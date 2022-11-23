import pygame
import sys
import pygame.font
import cv2


# initializing the constructor
pygame.init()

# screen resolution
res = (1000, 700)

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
orange = (255,215,0)

# opens up a window

# white color
color = (255,255,255)

# light shade of the button
color_light = (170,170,170)

# dark shade of the button
color_dark = (100,100,100)

# stores the width of the
# screen into a variable

# stores the height of the
# screen into a variable

# defining a font
#smallfont = pygame.font.SysFont('Corbel',35)

# rendering a text written in
# this font
#text = smallfont.render('quit' , True , color)


"""my varibles that will change"""
captionText = "These is no caption"

cap = cv2.VideoCapture('AnimatedBackground.mp4')
success, img = cap.read()
shape = img.shape[1::-1]
#wn = pygame.display.set_mode(shape)
wn = pygame.display.set_mode(res)
width = wn.get_width()
height = wn.get_height()
clock = pygame.time.Clock()


def uiUpdates():
    mouse = pygame.mouse.get_pos()

    for ev in pygame.event.get():
		
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    #checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:
    
    #if the mouse is clicked on the
    # button the game is terminated
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                pygame.quit()
                sys.exit()
            
# fills the screen with a color
    
    #screen.fill((0,0,0))
    
    # stores the (x,y) coordinates into
    # the variable as a tuple
    
    # if mouse is hovered on a button it
    # changes to lighter shade
    
    # superimposing the text onto our button
    #screen.blit(text , (width/2+50,height/2))

    #my stuff
    
        

    mainImage = pygame.image.load("pythonAssistantLogo.png")
    #mainImage = pygame.transform.scale(mainImage, (50,50))
    wn.blit(mainImage, ((width/2)-(mainImage.get_width()/2),(height/2)-(mainImage.get_height()/2)))
    mainImage.get_rect().center = (width // 2, height // 2)

    
   
    font = pygame.font.Font('Font.ttf', 50)
    subText = font.render(captionText, True, orange)
    wn.blit(subText, ((width/2)-(subText.get_width()/2),height-100))

    #mystuff
    
    # updates the frames of the game
    pygame.display.update()
	
	
def updateVideo():
    global cap
    clock.tick(60)
    success, img = cap.read()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            success = False
    try:
        wn.blit(pygame.image.frombuffer(img.tobytes(), shape, "BGR"), (0, 0))
    except AttributeError as e:
        cap = cv2.VideoCapture('AnimatedBackground.mp4')
    uiUpdates()
    pygame.display.update()




