from operator import index
import pygame 
import math

from pygame.constants import AUDIO_U16LSB, CONTROLLER_BUTTON_B
from DALLLET import BALLET
from alien import Alien
# Create the game window
pygame.init()
pygame.font.init()
# Give the window a name
pygame.display.set_caption("My Game")
bullets=[]
DIR=1
pointfont==pygame.font.SysFont("Comic Sans MS",30)
# Set a variable for the screen
screen = pygame.display.set_mode((800,600))
shoot_sound=pygame.mixer.Sound("Shoot.wav")
#Get the screen rectange
screen_rect = screen.get_rect()
player_image=pygame.image.load("playership.png")
player_image=pygame.transform.scale(player_image,(100,150))
player_rect=player_image.get_rect()
player_rect.x=300
player_rect.y=450
player_right=False
player_left=False
aliens=[]
def create_aliens(level):
    columns=800/(150 + 20)
    columns=math.floor(columns)
    y=0
    for k in range(level):
        x=0
        for i in range (columns):
            aliens.append(Alien(x,y,screen))
            x+=150+20
        y+=75+20
        
create_aliens(3)
    

# Create a main loop for the game
while True:
    pygame.time.Clock().tick(440 )
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                player_right=True
            if event.key==pygame.K_LEFT:
                player_left=True
            if event.key==pygame.K_SPACE: 
                pygame.mixer.Sound.play(shoot_sound)
                bullets.append(BALLET(player_rect.center[0],player_rect.y,screen))
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                player_right=False
            if event.key==pygame.K_LEFT:
                player_left=False
    if player_right:
        player_rect.x+=1
    if player_left:
        player_rect.x-=1
    if player_rect.right>screen_rect.right:
        player_rect.right=screen_rect.right
    if player_rect.left<0:
        player_rect.left=0
  # Fill the screens background
    screen.fill((150,150,50))
    for b in bullets:
        b.update_position()
        b.blit_me()
    screen.blit(player_image,player_rect)
    for A in aliens: 
        A.moveme(DIR)
        if A.lose(player_rect)==True:
            pygame.quit()
        res=A.check(DIR)
        DIR=res[0]
        if res[1]==True:
            for al in aliens:
                al.rect.y+=10
        for b in bullets:
            K=A.killme(b)
            if K:
                del aliens[aliens.index(A)]
                del bullets[bullets.index(b)]
        A.blitme()
    if len(aliens)==0:
        pygame.quit()
  # Flip the screen
    pygame.display.flip()
