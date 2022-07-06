import pygame
import random
import math
#initialization of pygame
pygame.init()
#creating screen
screen = pygame.display.set_mode((736,600))
#title logo and background colour
pygame.display.set_caption("SHOOTING GAME")
image = pygame.image.load("spaceship.png")
pygame.display.set_icon(image)

#score 
score = 0

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
    x_change_e.append(0.3)
    y_change_e.append(0.2)


#bullet
bullets = []
y_change_b = 0.2

bullet_image = pygame.image.load("bullet.png")

bullet_state = "ready"
def player(x,y):
    screen.blit(player_image,(x,y))

def enemy(x,y,i):
    screen.blit(enemy_image[i],(x,y))
    
def bullet(x,y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bullet_image,(x,y))

def iscollision(x_axis_b,y_axis_b,x_axis_e,y_axis_e) :
    distance = math.sqrt(math.pow(x_axis_e - x_axis_b,2)+math.pow(y_axis_e - y_axis_b,2))
    if distance < 18 :
        return True 
    else :
        return False 
    


#existing for long time
exist = True
while exist:
    for event in pygame.event.get():
        #exist from screen
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
                bullets.append([x_axis_b, y_axis_b])
                bullet_state = "fire"
                # bullet(x_axis_b,y_axis_b)
                
                
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT :
                x_change = 0 
        
        
        

        
    # RGB = RED GREEN BLUE
    screen.fill((0,0,0))
    
#checking player within the boundaries if does then it stop
    
    x_axis += x_change 
    if x_axis <= 64 :
        x_axis = 64
    elif x_axis >= 672 :
        x_axis = 672
    
    player(x_axis,y_axis) 
        
    for i in range(len(x_axis_e)):
        #checking enemy within the boundaries if exits then bounce it back
        x_axis_e[i] += x_change_e[i]
        if x_axis_e[i] <= 64 :
            x_change_e[i] = 0.3
        elif x_axis_e[i] >= 672 :
            x_change_e[i] = -0.3
        
        y_axis_e[i] += y_change_e[i]
        if y_axis_e[i] <= 50 :
            y_change_e[i] = 0.1
    
        enemy(x_axis_e[i],y_axis_e[i],i) 
        
        # if bullet_state == "fire" :
        #     bullet(x_axis_b,y_axis_b)
            
            
        # for bullet in bullets :
            
        collision = iscollision(bullet[0],bullet[1],x_axis_e[i],y_axis_e[i]) 
        if collision:
            enemy.remove(enemy_image[i])
            score += 25 
            x_axis_e[i] = random.randint(128,672)
            y_axis_e[i] = random.randint(50,150)
                    

    for bullet in bullets:
        screen.blit(bullet_image, (bullet[0] , bullet[1]))
        bullet[1] -= y_change_b
    
    for bullet in bullets:
        if bullet[1] < 0 - bullet_image.get_height():
            bullets.remove(bullet)
    
    
    
    
    
    pygame.display.update()
