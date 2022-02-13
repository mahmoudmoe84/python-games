import pygame
import os
WIDTH , HEIGHT = 1200,800
WIN  = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("First Game Ever!")

BLACK =(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
YELLOW = (255,255,0)
BORDER = pygame.Rect(595,0,10,HEIGHT)


FPS = 60
VEL=5
BULLETS_VEL = 7
MAX_BULLET = 3
SPACE_SHIP_WIDTH , SPACE_SHIP_HEIGHT = 55,40

YELLOW_HIT = pygame.USEREVENT+1
RED_HIT = pygame.USEREVENT+2

YELLOW_SPACESHIP =pygame.image.load(os.path.join('python-games1','spaceship_yellow.png'))
YELLOW_SPACESHIP= pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP,(SPACE_SHIP_WIDTH,SPACE_SHIP_HEIGHT)),90)
RED_SPACESHIP =pygame.image.load(os.path.join('python-games1','spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP,(SPACE_SHIP_WIDTH,SPACE_SHIP_HEIGHT)),270)

def yellow_handle_movement(key_pressed,yellow):
    if key_pressed[pygame.K_a] and yellow.x-VEL>0:#left
        yellow.x-=VEL
    if key_pressed[pygame.K_d] and yellow.x + VEL+yellow.width <BORDER.x:#right
        yellow.x+=VEL
    if key_pressed[pygame.K_w] and yellow.y-VEL>0:#up
        yellow.y-=VEL
    if key_pressed[pygame.K_s] and yellow.y+VEL+yellow.height<HEIGHT-10:#down
        yellow.y+=VEL

def red_handle_movement(key_pressed,red):
    if key_pressed[pygame.K_LEFT] and red.x - VEL>BORDER.x+BORDER.width:#left
        red.x-=VEL
    if key_pressed[pygame.K_RIGHT] and red.x+VEL+red.width<WIDTH:#right
        red.x+=VEL
    if key_pressed[pygame.K_UP] and red.y - VEL >0:#up
        red.y-=VEL
    if key_pressed[pygame.K_DOWN] and red.y +VEL +red.height<HEIGHT-10:#down
        red.y+=VEL 

def handle_bullets(yellow_bullets,red_bullets,yellow,red):
    for bullet in yellow_bullets:
        bullet.x+=BULLETS_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x-=BULLETS_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)

def draw_window(red,yellow,red_bullets,yellow_bullets):
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x,red.y))
    pygame.draw.rect(WIN,BLACK,BORDER)
    
    
    for bullet in red_bullets:
        pygame.draw.rect(WIN,RED,bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN,YELLOW,bullet)
        
    pygame.display.update()
def main():
    
    red = pygame.Rect(900,350,SPACE_SHIP_WIDTH , SPACE_SHIP_HEIGHT)
    yellow = pygame.Rect(200,350,SPACE_SHIP_WIDTH , SPACE_SHIP_HEIGHT)
    
    red_bullets =[]    
    yellow_bullets = []

    Clock = pygame.time.Clock()
    run = True
    while run:
        Clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets)<MAX_BULLET:
                    bullet=pygame.Rect(yellow.x+yellow.width,yellow.y+yellow.height//2-2,10,5)
                    yellow_bullets.append(bullet)
                
                if event.key == pygame.K_RCTRL and len(red_bullets)<MAX_BULLET:    
                    bullet=pygame.Rect(red.x,red.y+red.height//2-2,10,5)
                    red_bullets.append(bullet)
        
        draw_window(red,yellow,red_bullets,yellow_bullets)        
        key_pressed = pygame.key.get_pressed()
        yellow_handle_movement(key_pressed,yellow)
        red_handle_movement(key_pressed,red)       
        
        handle_bullets(yellow_bullets,red_bullets,yellow,red)
    
    pygame.quit()

    
if __name__ =="__main__":
    main()
