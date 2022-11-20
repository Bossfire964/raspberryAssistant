import pygame
import sys
import pygame.font



# initializing the constructor
pygame.init()

# screen resolution
res = (720, 720)

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

# opens up a window
screen = pygame.display.set_mode(res)

# white color
color = (255,255,255)

# light shade of the button
color_light = (170,170,170)

# dark shade of the button
color_dark = (100,100,100)

# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()

# defining a font
#smallfont = pygame.font.SysFont('Corbel',35)

# rendering a text written in
# this font
#text = smallfont.render('quit' , True , color)


"""my varibles that will change"""
captionText = "These is no caption"


def uiUpdates():
    mouse = pygame.mouse.get_pos()

    for ev in pygame.event.get():
		
        if ev.type == pygame.QUIT:
            pygame.quit()
            return True
        
    #checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:
    
    #if the mouse is clicked on the
    # button the game is terminated
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                pygame.quit()
                return True
            
# fills the screen with a color
    
    screen.fill((0,0,0))
    
    # stores the (x,y) coordinates into
    # the variable as a tuple
    
    # if mouse is hovered on a button it
    # changes to lighter shade
    
    # superimposing the text onto our button
    #screen.blit(text , (width/2+50,height/2))

    #my stuff
    mainImage = pygame.image.load("MoneyIcon.bmp")
    screen.blit(mainImage, (width-520,height-520))
    mainImage.get_rect().center = (width // 2, height // 2)
   
    font = pygame.font.Font('freesansbold.ttf', 32)
    subText = font.render(captionText, True, green)
    screen.blit(subText, (width-520,height-100))

    topText = font.render(captionText, True, green)
    screen.blit(topText, (width-520,100))

    #mystuff
    
    # updates the frames of the game
    pygame.display.update()
	
	





