
#!/usr/bin/env python

from __future__ import print_function

import argparse
import os.path
import json
import time
import speechrecognition
import asyncio

import speech_recognition as sr

import google.oauth2.credentials
import RPi.GPIO as GPIO
from google.assistant.library import Assistant
from google.assistant.library.event import EventType
from google.assistant.library.file_helpers import existing_file


if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(25, GPIO.OUT)
    GPIO.setup(14, GPIO.OUT)
    p = GPIO.PWM(14,50)
    p.start(2.5)
    p.ChangeDutyCycle(0)
    GPIO.output(25,False)
speaking = False
def doCommand(info, p):
    if info == "light on":
        p.ChangeDutyCycle(4.1)
        time.sleep(1)
        p.ChangeDutyCycle(0)
        return True
    if info == "light off" or info == "light of" or info == "turn light off" or info == "turn light of":
        p.ChangeDutyCycle(11.33)
        time.sleep(1)
        p.ChangeDutyCycle(0)
        return True
    return False
def process_event(event, assistant):
    """Pretty prints events.
    Prints all events that occur with two spaces between each new
    conversation and a single space between turns of a conversation.
    Args:
        event(event.Event): The current event to process.
    """
    if event.type == EventType.ON_CONVERSATION_TURN_STARTED:
        print()
        GPIO.output(25,True)

    print(event)
    if event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED:
        speech = event.args["text"]
        customCommand = doCommand(speech, p)
        
        if customCommand:
            assistant.stop_conversation()
        
    if (event.type == EventType.ON_CONVERSATION_TURN_FINISHED and
            event.args and not event.args['with_follow_on_turn']):
        print()
        GPIO.output(25,False)
        speaking = False
async def showQues(assistant):
    while True:
        item = assistant.get()
        process_event(item)
def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--credentials', type=existing_file,
                        metavar='OAUTH2_CREDENTIALS_FILE',
                        default=os.path.join(
                            os.path.expanduser('/home/pi/.config'),
                            'google-oauthlib-tool',
                            'credentials.json'
                        ),
                        help='Path to store and read OAuth2 credentials')
    args = parser.parse_args()
    with open(args.credentials, 'r') as f:
        credentials = google.oauth2.credentials.Credentials(token=None,
                                                            **json.load(f))

    with Assistant(credentials, "yes") as assistant:
        ques = assistant.start()
        #loop = asyncio.get_event_loop()
        #loop.run_until_complete(showQues(ques))
        while True:
             output = speechrecognition.record_audio(p)
             if output == True:
                 GPIO.output(25,True)
                 assistant.start_conversation()
                 speaking = True
                 while speaking:
                     item = ques.get()
                     process_event(item, assistant)
                     if (item.type == EventType.ON_CONVERSATION_TURN_FINISHED and
            item.args and not item.args['with_follow_on_turn']):
                         break;
                     if item.type == EventType.ON_ASSISTANT_ERROR:
                         GPIO.output(25, False)
                         break;
                    
                    
             
        
            
if __name__ == '__main__':
    main()


    







