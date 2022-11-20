import speech_recognition
import pyttsx3
import time
import assistant

wakeWord = "computer"

awake = False

rec = speech_recognition.Recognizer()
def record_audio(p):
    print("aliot")
    rec = speech_recognition.Recognizer()
    try:
        with speech_recognition.Microphone(device_index=2) as mic:
            rec.adjust_for_ambient_noise(mic, duration=0.1)
            audio = rec.listen(mic)
            
            text = rec.recognize_google(audio)
            text = text.lower()
            
            if text.split()[0] == wakeWord:
                print("woken")
                print(text[len(wakeWord)+1:len(text)-1])
                if not assistant.doCommand(text[len(wakeWord)+1:len(text)], p):
                    return True
        
            print("Recognized " + text)
    except Exception as error:
        rec = speech_recognition.Recognizer()
        print(error)