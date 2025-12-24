import pygame
from sys import exit
import random
from value import *
import pygame_gui

pygame.init()
screen = pygame.display.set_mode((800,450))
pygame.display.set_caption('ArrowMatcher')
clock = pygame.time.Clock()
MANAGER= pygame_gui.UIManager((800,450))

Ar_=random.choice(Ar)
Ar1_rect=Ar_.get_rect(center=(450,400))

font=pygame.font.Font(None,50)
font1=pygame.font.Font(None,45)
font3=pygame.font.Font(None,70)

text1 = font3.render("Start",True,"Blue")
tx1_rect=text1.get_rect(center=(400,225))

text3 = font.render("pause(restart press enter)",True,"Yellow")
tx3_rect=text3.get_rect(center=(400,225))

text4 = font.render("leaderboard",True,"Orange")
tx4_rect=text4.get_rect(center=(135,390))

text5 = font.render("name",True,"Orange")
tx5_rect=text5.get_rect(center=(320,270))

score=0
input_rect = pygame.Rect(200, 200, 140, 32)
work=False



input_text = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((350,270),(100,45)),manager=MANAGER,object_id="enter_name")
hexa=15
exp=400
active=False

Bs1=pygame.mixer.Sound("music/Bs1.mp3")
Bs1.play(loops = -1)
try:
    while True:
        hexa+=1
        ui_refresh_rate=clock.tick(60)/1000
        
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ended()
                pygame.quit()
                exit

            MANAGER.process_events(event)

            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.key == pygame.K_UP and Ar_== Ar1 or event.key == pygame.K_RIGHT and Ar_ == Ar2  or event.key == pygame.K_DOWN and Ar_ == Ar3 or event.key == pygame.K_LEFT and Ar_ == Ar4:
                    if Ar1_rect.midtop[1]>250 and Ar1_rect.midbottom[1]<310:
                        score+=1
                        Ar_=random.choice(Ar)
                        Ar1_rect.top = 500
                    else:
                        pass

            

                if event.key == pygame.K_SPACE:
                    meta=0
                    while True:
                        meta+=1
                        if meta == 3:
                            screen.blit(text3,tx3_rect)
                            if event.key == pygame.K_SPACE:
                                break
                            
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "enter_name":
                work=True
                name=event.text
                
        MANAGER.update(ui_refresh_rate)
        
             
        #game started        
        if score > 0:
            check(score,name)
            
                        
            #for games speed
            if score > 20:
                hff=(score-20)/10
                speed=4+hff

            else:
                speed=4
            #for background
            if hexa > 15:
                hexa=0
                Bg_=back_new()
            screen.blit(Bg_,(0,0))
                
            #for border
            screen.blit(Bor,(415,250))

            #display score
            text2 = font.render("Score:"+str(score),True,"Yellow")
            tx2_rect=text1.get_rect(center=(70,25))
            screen.blit(text2,tx2_rect)
            

            #for arrow motion
            
            screen.blit(Ar_,Ar1_rect)
            Ar1_rect.top -= speed
            if Ar1_rect.top <= 200:
                Ar_=random.choice(Ar)
                Ar1_rect.top = 500
                score-=1

        #game ends
        if score == 0:
            leaders=leader()
            hexa=400
            if hexa == 400:
                hexa=0
                Gs_=game_new()

            screen.blit(Gs_,(0,0))


            mouse_pos=pygame.mouse.get_pos()
            screen.blit(text1,tx1_rect)
            screen.blit(text4,tx4_rect)

            if work == True:
                if tx1_rect.collidepoint(mouse_pos):
                    if pygame.mouse.get_pressed():
                            score=10
                            hexa=15

            text5 = font1.render(leaders,True,"Orange")

            MANAGER.draw_ui(screen)
            
            screen.blit(text5,(exp,400))
            exp-=2
            if exp == -40:
                exp = 900

        pygame.display.update()
            
        
        clock.tick(30)


except pygame.error:
    pass
