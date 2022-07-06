import math
from turtle import distance
import pygame
import random
#initialization of pygame
pygame.init()
#creating screen
screen = pygame.display.set_mode((736,600))
#title logo and background colour
pygame.display.set_caption("SHOOTING GAME")
image = pygame.image.load("spaceship.png")
pygame.display.set_icon(image)

#player
player_image = pygame.image.load("spaceship.png")
x_axis = 400
y_axis = 470
x_change = 0

#enemy
enemy_image = []
x_axis_e = []
y_axis_e = []
x_change_e = []
y_change_e = []

for i in range(4):
        enemy_image.append(pygame.image.load("allien.png"))
        x_axis_e.append(random.randint(128,672))
        y_axis_e.append(random.randint(50,150))
        x_change_e.append(0.04)
        y_change_e.append(0.04)
        
def enemy(x,y,i):
    screen.blit(enemy_image[i],(x,y))

#score board

score = 0
font_p = pygame.font.Font("freesansbold.ttf",32)

text_x = 10
text_y = 10

def show_s(x,y) :
    show = font_p.render("SCORE : " + str(score), True , (255,0 , 0))
    screen.blit(show,(x,y))

# enemy score 

score_e = 0
font_e = pygame.font.Font("freesansbold.ttf",32)

text_x_e = 500
text_y_e = 10

def show_e(x,y) :
    show = font_e.render("ENEMY : " + str(score_e), True , (255,0 , 0))
    screen.blit(show,(x,y))
    
# gameover

game_x = 75
game_y = 300

font_g = pygame.font.Font("freesansbold.ttf",75)
def game_over(x,y) :
    show = font_g.render("  GAME OVER " , True , (255,0 , 0))
    screen.blit(show,(x,y))



bullet_state = "ready"
def player(x,y):
    screen.blit(player_image,(x,y))

bullet_image = pygame.image.load("bullet.png")
x_axis_b = 400
y_axis_b = 450
x_change_b = 0
y_change_b = 0.2
    
def bullet(x,y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bullet_image,(x,y))
    
def collision(x_axis_e,y_axis_e,x_axis_b,y_axis_b):
    distance = math.sqrt(math.pow(x_axis_e - x_axis_b,2)+math.pow(y_axis_e - y_axis_b,2))
    if distance < 18 :
        return True 
    else :
        return False 

exist = True
while exist:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            exist  = False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT :
                x_change = -0.2   
            if event.key == pygame.K_RIGHT :
                x_change = 0.2 
            if event.key == pygame.K_SPACE :
                x_axis_b = x_axis
                y_axis_b = y_axis
                bullet_state = "fire"
                
                
                
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT :
                x_change = 0 
                 
    

        
    #RGB = RED GREEN BLUE
    screen.fill((0,0,0))
    
    #checking player within the boundaries if does then it stop
    
    x_axis += x_change 
    if x_axis <= 64 :
        x_axis = 64
    elif x_axis >= 672 :
        x_axis = 672
    
    player(x_axis,y_axis) 
        
    for i in range(4):
        
        x_axis_e[i] += x_change_e[i]
        if x_axis_e[i] <= 64 :
            x_change_e[i] = 0.1
        elif x_axis_e[i] >= 672 :
            x_change_e[i] = -0.1
        
        y_axis_e[i] += y_change_e[i]
        if y_axis_e[i] <= 50 :
            y_change_e[i] = 0.1
    
        enemy(x_axis_e[i],y_axis_e[i],i)
        
        iscollision = collision(x_axis_e[i],y_axis_e[i],x_axis_b,y_axis_b)
        if iscollision :
            
            bullet_state = "ready"
            y_axis_b = 450
            score += 25
            x_axis_e[i] = random.randint(128,672)
            y_axis_e[i] = random.randint(50,150)
        
        if y_axis_e[i] >= 500 and y_axis_e[i] <= 501 :
            
            score_e += 1
            
    if score_e == 100 :
        game_over (game_x,game_y)
                
            
    if y_axis_b <= 0 :
        y_axis_b = 450
        bullet_state = "ready"

    if bullet_state ==  "fire" :
        bullet(x_axis_b,y_axis_b)
        y_axis_b -= y_change_b
    
    show_s (text_x,text_y)
        
    show_e (text_x_e ,text_y_e)
    
    
        
        
    
    pygame.display.update()
    