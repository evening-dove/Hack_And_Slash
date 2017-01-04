import pygame
from pygame.locals import *
pygame.init()

import os
import random

import classes
import functions

size=(640, 480)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Yeah, Pygame!")


base_dirr=os.getcwd()
img_dirr=base_dirr+"/images"


helvet=pygame.font.match_font("Helvetica", True, False)
menu_font=pygame.font.Font(helvet, 16)
instructions_font=pygame.font.Font(helvet, 14)

cass_font=pygame.font.match_font("alphabetized cassette tapes", True, False)
password_font=pygame.font.Font(cass_font, 100)

digital_font=pygame.font.match_font("", True, False)
keypad_display_font=pygame.font.Font(digital_font, 50)


#define mouse
mouse=classes.Mouse()
m_group=pygame.sprite.Group(mouse)

#Creates player
player=classes.Player(img_dirr)
player_group=pygame.sprite.Group(player)

#Creates Enemy                                 
enemy=classes.Enemy(img_dirr)
enemy_group=pygame.sprite.Group(enemy)













os.chdir(img_dirr+"/backgrounds")
wall=pygame.image.load("walls.bmp").convert()
wall=pygame.transform.scale(wall, (int(wall.get_size()[0]*2.5), int(wall.get_size()[1]*2.5)))
walls_counter=0

#Creates door frames

door_locations=[[-130, 0]] #door_locations=[[location, current frame]]

while door_locations[-1][0]-200>=-200:
    door_locations+=[[door_locations[-1][0]-200, 0]]

door_closing_frames=[]
for i in range(0,14):
    temp_frame=pygame.image.load("closing_frame_{}.bmp".format(i)).convert()
    temp_frame.set_colorkey((255,0,255))
    temp_frame=pygame.transform.scale(temp_frame, (int(temp_frame.get_size()[0]*2), int(temp_frame.get_size()[1]*3)))
    door_closing_frames+=[temp_frame]
    

console=pygame.image.load("console.bmp".format(i)).convert()
console.set_colorkey((255,0,255))
console=pygame.transform.scale(console, (int(console.get_size()[0]*.8), int(console.get_size()[1]*.8)))







os.chdir(img_dirr+"/ui")


in_menu=True
in_main_menu=True
in_instructions_menu=False
in_game_over_menu=False




main_menu=pygame.image.load("main_menu.bmp").convert()
main_menu.set_colorkey((255,0,255))
main_menu_rect=main_menu.get_rect()
main_menu_rect.centerx=size[0]/2
main_menu_rect.centery=(size[1]/2)+10

menu_divider=pygame.Surface((150,3)).convert()
menu_divider.fill((23,50,57))   

start_game_button=pygame.Surface((200,30)).convert()
start_game_button.fill((0,0,0)) 
start_game_button.set_alpha(0)
start_game_button_rect=start_game_button.get_rect()
start_game_button_rect.centerx=size[0]/2
start_game_button_rect.centery=164
start_game_text=menu_font.render("Start Game", True, (255,255,255))
start_game_text_rect=start_game_text.get_rect()
start_game_text_rect.centerx=start_game_button_rect.centerx
start_game_text_rect.centery=start_game_button_rect.centery

difficulty_text=menu_font.render("Difficulty:", True, (255,255,255))
difficulty_text_rect=difficulty_text.get_rect()
difficulty_text_rect.centerx=size[0]/2
difficulty_text_rect.centery=197

difficulty_1_button=pygame.Surface((50,30)).convert()
difficulty_1_button.fill((0,0,0)) 
difficulty_1_button.set_alpha(0)
difficulty_1_button_rect=difficulty_1_button.get_rect()
difficulty_1_button_rect.centerx=size[0]/2-75
difficulty_1_button_rect.centery=227
difficulty_1_text=menu_font.render("1", True, (255,255,255))
difficulty_1_text_rect=difficulty_1_text.get_rect()
difficulty_1_text_rect.centerx=difficulty_1_button_rect.centerx
difficulty_1_text_rect.centery=difficulty_1_button_rect.centery

difficulty_2_button=pygame.Surface((50,30)).convert()
difficulty_2_button.fill((0,0,0)) 
difficulty_2_button.set_alpha(0)
difficulty_2_button_rect=difficulty_1_button.get_rect()
difficulty_2_button_rect.centerx=size[0]/2-25
difficulty_2_button_rect.centery=227
difficulty_2_text=menu_font.render("2", True, (255,255,255))
difficulty_2_text_rect=difficulty_1_text.get_rect()
difficulty_2_text_rect.centerx=difficulty_2_button_rect.centerx
difficulty_2_text_rect.centery=difficulty_2_button_rect.centery

difficulty_3_button=pygame.Surface((50,30)).convert()
difficulty_3_button.fill((0,0,0)) 
difficulty_3_button.set_alpha(0)
difficulty_3_button_rect=difficulty_3_button.get_rect()
difficulty_3_button_rect.centerx=size[0]/2+25
difficulty_3_button_rect.centery=227
difficulty_3_text=menu_font.render("3", True, (255,255,255))
difficulty_3_text_rect=difficulty_3_text.get_rect()
difficulty_3_text_rect.centerx=difficulty_3_button_rect.centerx
difficulty_3_text_rect.centery=difficulty_3_button_rect.centery

difficulty_4_button=pygame.Surface((50,30)).convert()
difficulty_4_button.fill((0,0,0)) 
difficulty_4_button.set_alpha(0)
difficulty_4_button_rect=difficulty_4_button.get_rect()
difficulty_4_button_rect.centerx=size[0]/2+75
difficulty_4_button_rect.centery=227
difficulty_4_text=menu_font.render("4", True, (255,255,255))
difficulty_4_text_rect=difficulty_4_text.get_rect()
difficulty_4_text_rect.centerx=difficulty_4_button_rect.centerx
difficulty_4_text_rect.centery=difficulty_4_button_rect.centery


difficulty_underline=pygame.Surface((20,3)).convert()
difficulty_underline.fill((110,110,110))  


how_to_play_button=pygame.Surface((200,30)).convert()
how_to_play_button.fill((0,0,0)) 
how_to_play_button.set_alpha(0)
how_to_play_button_rect=how_to_play_button.get_rect()
how_to_play_button_rect.centerx=size[0]/2
how_to_play_button_rect.top=270
how_to_play_text=menu_font.render("How to Play", True, (255,255,255))
how_to_play_text_rect=how_to_play_text.get_rect()
how_to_play_text_rect.centerx=how_to_play_button_rect.centerx
how_to_play_text_rect.top=how_to_play_button_rect.top


instructions_back_button=pygame.Surface((200,30)).convert()
instructions_back_button.fill((0,0,0)) 
instructions_back_button.set_alpha(0)
instructions_back_button_rect=instructions_back_button.get_rect()
instructions_back_button_rect.centerx=size[0]/2
instructions_back_button_rect.top=370
instructions_back_text=menu_font.render("Back", True, (255,255,255))
instructions_back_text_rect=instructions_back_text.get_rect()
instructions_back_text_rect.centerx=instructions_back_button_rect.centerx
instructions_back_text_rect.top=instructions_back_button_rect.top


####
#Creates the text for the instructions screen

instructions_menu=pygame.image.load("main_menu.bmp").convert()
instructions_menu=pygame.transform.scale(instructions_menu, (400, instructions_menu.get_size()[1]))
instructions_menu.set_colorkey((255,0,255))
instructions_menu_rect=instructions_menu.get_rect()
instructions_menu_rect.centerx=size[0]/2
instructions_menu_rect.centery=(size[1]/2)+10

instructions_text_1=instructions_font.render("The final Villain has just been defeated, and it's time to make", True, (255,255,255))
instructions_text_2=instructions_font.render("your heroic escape! But what's this? The Villain is still alive,", True, (255,255,255))
instructions_text_3=instructions_font.render("the facility is set to explode, and the only escape route is on", True, (255,255,255))
instructions_text_4=instructions_font.render("lockdown! Type your way through the doors on one front,", True, (255,255,255))
instructions_text_5=instructions_font.render("while blocking a flurry of attacks on the other. How long can ", True, (255,255,255))
instructions_text_6=instructions_font.render("you survive?", True, (255,255,255))
instructions_text_7=instructions_font.render("Use the Keyboard to type in passwords as", True, (255,255,255))
instructions_text_8=instructions_font.render("they appear on screen.", True, (255,255,255))
instructions_text_9=instructions_font.render("The Villain will strike high, medium, or low. Use the", True, (255,255,255))
instructions_text_10=instructions_font.render("Scroll Wheel to match your strike to theirs. Once it matches,", True, (255,255,255))
instructions_text_11=instructions_font.render("use Left Click to block the attack.", True, (255,255,255))




#Creates the game over screen
game_end_menu=main_menu
game_end_menu_rect=game_end_menu.get_rect()
game_end_menu_rect.centerx=size[0]/2
game_end_menu_rect.centery=size[1]/2+10

final_score_text=menu_font.render("Final Score:", True, (255,255,255))

replay_button=pygame.Surface((200,30)).convert()
replay_button.fill((0,0,0)) 
replay_button.set_alpha(0)
replay_button_rect=replay_button.get_rect()
replay_button_rect.centerx=size[0]/2
replay_button_rect.centery=330
replay_text=menu_font.render("Replay", True, (255,255,255))
replay_text_rect=replay_text.get_rect()
replay_text_rect.centerx=replay_button_rect.centerx
replay_text_rect.centery=replay_button_rect.centery

return_main_button=pygame.Surface((200,30)).convert()
return_main_button.fill((0,0,0)) 
return_main_button.set_alpha(0)
return_main_button_rect=return_main_button.get_rect()
return_main_button_rect.centerx=size[0]/2
return_main_button_rect.centery=363
return_main_text=menu_font.render("Main Menu", True, (255,255,255))
return_main_text_rect=return_main_text.get_rect()
return_main_text_rect.centerx=return_main_button_rect.centerx
return_main_text_rect.centery=return_main_button_rect.centery








keypad_display=pygame.image.load("keypad_display.bmp").convert()
keypad_display.set_colorkey((255,0,255))
keypad_display=pygame.transform.scale(keypad_display, (250, 70))


paper=pygame.image.load("paper.bmp").convert()
paper.set_colorkey((255,0,255))
paper=pygame.transform.scale(paper, (int(paper.get_size()[0]*.5), int(paper.get_size()[1]*.5)))


background=pygame.Surface(size)
background=background.convert()


background.fill((40, 32, 24))

top_bottom_clear=pygame.Surface((size[0], 300)).convert()
top_bottom_clear.fill((40, 32, 24))



clock=pygame.time.Clock()
keep_going=True

clicked=False

difficulty=0

dead_counter=0
clash_counter=0

password=functions.make_passwords(player.doors_opened, difficulty)
password_progress=""
at_panel=False


while keep_going:
    
    clicked=False
    
    clock.tick(30)
    
    
    for ev in pygame.event.get():
            
        if ev.type==QUIT:
            keep_going=False
            
        if ev.type==MOUSEMOTION:
            mouse.x=ev.pos[0]
            mouse.y=ev.pos[1]
        
        if ev.type==MOUSEBUTTONDOWN:
            
            if in_menu==False and dead_counter==0:
                if ev.button==4:
                    if player.parry_location=="middle":
                        player.parry_location="top"
                    elif player.parry_location=="bottom":
                        player.parry_location="middle"
                if ev.button==5:
                    if player.parry_location=="top":
                        player.parry_location="middle"
                    elif player.parry_location=="middle":
                        player.parry_location="bottom"
                    
            if ev.button==1:
                if in_menu==False and dead_counter==0:
                    if enemy.attacking==True and player.block_counter!=0:
                        if enemy.attack_location==player.parry_location:
                            player.attacks_blocked+=1
                            enemy.attacking=False
                            if enemy.attack_location=="top":
                                enemy.rect.left-=40
                            if enemy.attack_location=="middle":
                                enemy.rect.left-=30
                            if enemy.attack_location=="bottom":
                                enemy.rect.left-=30
                            clash_counter=20
                        if enemy.attack_location!=player.parry_location:
                            player.block_counter=1
                    
        
                
                
        if ev.type==MOUSEBUTTONUP:
            if ev.button==1:
                clicked=True
                
                
                
        if ev.type==KEYDOWN:
            if in_menu==False and dead_counter==0 and at_panel==True:
                letter_keys=[K_q, K_w, K_e, K_r, K_t, K_y, K_u, K_i, K_o, K_p, K_a, K_s, K_d, K_f, K_g, K_h, K_j, K_k, K_l, K_z, K_x, K_c, K_v, K_b, K_n, K_m]
                num_keys=[K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9, K_0]
                
                if ev.key in letter_keys or ev.key in num_keys:
                
                    keys=pygame.key.get_pressed()
                    if ev.key in letter_keys:
                        key_typed=["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"][letter_keys.index(ev.key)]
                        if keys[K_LSHIFT]==True or keys[K_RSHIFT]==True:
                            key_typed=key_typed.upper()
                            
                            
                    if ev.key in num_keys:
                        key_typed=["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"][num_keys.index(ev.key)]
                        
                    if password[len(password_progress)]==key_typed:
                        password_progress+=key_typed
                    elif password[len(password_progress)]!=key_typed:
                        password_progress=""
                        player.wrong_key_penalty+=1
                    
            
            
    
    if in_menu==True:
        
        
        
        if in_main_menu==True:
            collisions=mouse.rect.colliderect(start_game_button_rect)
            if collisions==1 and clicked==True:
                in_menu=False
                in_main_menu=False
                
            collisions=mouse.rect.colliderect(difficulty_1_button_rect)
            if collisions==1 and clicked==True:
                difficulty=0
                
            collisions=mouse.rect.colliderect(difficulty_2_button_rect)
            if collisions==1 and clicked==True:
                difficulty=1
                
            collisions=mouse.rect.colliderect(difficulty_3_button_rect)
            if collisions==1 and clicked==True:
                difficulty=2
                
            collisions=mouse.rect.colliderect(difficulty_4_button_rect)
            if collisions==1 and clicked==True:
                difficulty=3
                
            collisions=mouse.rect.colliderect(how_to_play_button_rect)
            if collisions==1 and clicked==True:
                in_main_menu=False
                in_instructions_menu=True
            
            
        if in_instructions_menu==True:
                
            collisions=mouse.rect.colliderect(instructions_back_button_rect)
            if collisions==1 and clicked==True:
                in_instructions_menu=False
                in_main_menu=True
                
                background.blit(top_bottom_clear, (0,0))
                background.blit(top_bottom_clear, (0,340))
                
                
        if in_game_over_menu==True:
            reset_game=False
            collisions=mouse.rect.colliderect(replay_button_rect)
            if collisions==1 and clicked==True:
                reset_game=True
                in_menu=False
                in_game_over_menu=False
                
            collisions=mouse.rect.colliderect(return_main_button_rect)
            if collisions==1 and clicked==True:
                reset_game=True
                in_main_menu=True
                in_game_over_menu=False
                
                background.blit(top_bottom_clear, (0,0))
                background.blit(top_bottom_clear, (0,340))
                
                
            if reset_game==True:
                player.rect.bottom=300
                player.rect.left=300
                
                enemy.rect.bottom=300
                enemy.rect.left=380   
                
                
                player.doors_opened=0
                player.attacks_blocked=0
                player.wrong_key_penalty=0
                
                enemy.attacking=False
                
                door_locations=[[-130, 0]]
            
                while door_locations[-1][0]-200>=-200:
                    door_locations+=[[door_locations[-1][0]-200, 0]]
                
                at_panel=False
            
            
                
                
                
        
        if in_game_over_menu==False:
            walls_x=0
            while walls_x<size[0]:
                background.blit(wall, (walls_x, 100))
                walls_x+=wall.get_size()[0]
            
            
        if in_main_menu==True: 
            background.blit(main_menu, main_menu_rect)
            background.blit(start_game_button, start_game_button_rect)
            background.blit(start_game_text, start_game_text_rect)
            background.blit(menu_divider, (size[0]/2-75, 179))
            background.blit(difficulty_text, difficulty_text_rect)
            background.blit(difficulty_1_button, difficulty_1_button_rect)
            background.blit(difficulty_1_text, difficulty_1_text_rect)
            background.blit(difficulty_2_button, difficulty_2_button_rect)
            background.blit(difficulty_2_text, difficulty_2_text_rect)
            background.blit(difficulty_3_button, difficulty_3_button_rect)
            background.blit(difficulty_3_text, difficulty_3_text_rect)
            background.blit(difficulty_4_button, difficulty_4_button_rect)
            background.blit(difficulty_4_text, difficulty_4_text_rect)
            background.blit(difficulty_underline, (size[0]/2-75-difficulty_underline.get_size()[0]/2+50*difficulty, 242))
            background.blit(menu_divider, (size[0]/2-75, 260))
            background.blit(how_to_play_button, how_to_play_button_rect)
            background.blit(how_to_play_text, how_to_play_text_rect)
            
        ####
        if in_instructions_menu==True:
            background.blit(instructions_menu, instructions_menu_rect)
            background.blit(instructions_text_1, (144, 160))
            background.blit(instructions_text_2, (144, 175))
            background.blit(instructions_text_3, (144, 190))
            background.blit(instructions_text_4, (144, 205))
            background.blit(instructions_text_5, (144, 220))
            background.blit(instructions_text_6, (144, 235))
            background.blit(instructions_text_7, (144, 260))
            background.blit(instructions_text_8, (144, 275))
            background.blit(instructions_text_9, (144, 290))
            background.blit(instructions_text_10, (144, 305))
            background.blit(instructions_text_11, (144, 320))
            background.blit(menu_divider, (size[0]/2-75, 360))
            background.blit(instructions_back_button, instructions_back_button_rect)
            background.blit(instructions_back_text, instructions_back_text_rect)
            
            
            
            
        if in_game_over_menu==True:
            
                   
            
            door_score_text=menu_font.render("You opened "+str(player.doors_opened)+" Doors", True, (255,255,255))
            block_score_text=menu_font.render("And Blocked "+str(player.attacks_blocked)+" Attacks", True, (255,255,255))
            player_score_text=menu_font.render(str(player.doors_opened*100+player.attacks_blocked*30), True, (255,255,255))
            
            
            background.blit(game_end_menu, game_end_menu_rect)
            
            background.blit(door_score_text, ((int(size[0]-door_score_text.get_size()[0])/2), 170))
            background.blit(block_score_text, ((int(size[0]-block_score_text.get_size()[0])/2), 190))
            background.blit(final_score_text, ((int(size[0]-final_score_text.get_size()[0])/2), 240))
            background.blit(player_score_text, ((int(size[0]-player_score_text.get_size()[0])/2), 260))
            
            
            background.blit(replay_button, replay_button_rect)
            background.blit(replay_text, replay_text_rect)
            background.blit(menu_divider, (size[0]/2-75, 345))
            background.blit(return_main_button, return_main_button_rect)
            background.blit(return_main_text, return_main_text_rect)
            
            
            
            
            
        
        
    
    
    if in_menu==False:
        
        if door_locations[player.doors_opened][0]==195:
            password=functions.make_passwords(player.doors_opened, difficulty)
            password_progress=""
            at_panel=True
            enemy.attack_counter=10
            enemy.attack_location="none"
            paper=pygame.image.load("paper.bmp").convert()
            paper.set_colorkey((255,0,255))
            paper=pygame.transform.scale(paper, (int(paper.get_size()[0]*.5), int(paper.get_size()[1]*.5)))
            password_text=password_font.render(password, True, (0,0,0))
            paper.blit(password_text, (75, 40))
        
        
        
                       
        if door_locations[player.doors_opened][0]!=200:
            background.blit(top_bottom_clear, (0,0))
            background.blit(top_bottom_clear, (0,340))
            walls_counter+=5
            
            for i in range(0, len(door_locations)):
                
                door_locations[i][0]+=5
                
                if door_locations[i][0]>200 and door_locations[i][1]!=13:
                    door_locations[i][1]+=1
            
            if door_locations[-1][0]-200>=-200:
                door_locations+=[[door_locations[-1][0]-200, 0]]
            
            if walls_counter>0:
                walls_counter-=wall.get_size()[0]
        walls_x=walls_counter-wall.get_size()[0]
        while walls_x<size[0]:
            background.blit(wall, (walls_x, 100))
            walls_x+=wall.get_size()[0]
                                   
                                     
        if door_locations[player.doors_opened][0]==200:
            at_panel=True
                
                
        player.update(at_panel)
                          
        enemy.update(at_panel)
        
                
            
        if password_progress==password:
            player.doors_opened+=1
            password_progress=""
            at_panel=False
            enemy.attacking=False
            
            
            
        if dead_counter!=0:
            dead_counter-=1
            if dead_counter==0:
                in_menu=True
                in_game_over_menu=True
                
            
        if enemy.attacking==True:
            player.block_counter-=1
            if player.block_counter==0:
                if enemy.attack_location=="top":
                    enemy.rect.left-=70
                if enemy.attack_location=="middle":
                    enemy.rect.left-=50
                if enemy.attack_location=="bottom":
                    enemy.rect.left-=50
                    
                dead_counter=10
                
            
                    
                    
        if clash_counter!=0:
            clash_counter-=1
            if clash_counter==0:
                enemy.attack_counter=30
                if enemy.attack_location=="top":
                    enemy.rect.left+=40
                if enemy.attack_location=="middle":
                    enemy.rect.left+=30
                if enemy.attack_location=="bottom":
                    enemy.rect.left+=30
                enemy.attack_location="none"
            
            
        if at_panel==True and enemy.attack_counter!=0:
            enemy.attack_counter-=1
            if enemy.attack_counter==0:
                player.block_counter=max(1, 30-int(.5*player.doors_opened+.15*player.attacks_blocked+1/3*player.wrong_key_penalty*difficulty))
                attack_location=random.randrange(0,2)
                if attack_location==0:
                    if player.parry_location=="top":
                        enemy.attack_location="middle"
                    if player.parry_location!="top":
                        enemy.attack_location="top"
                if attack_location==1:
                    if player.parry_location!="bottom":
                        enemy.attack_location="bottom"
                    if player.parry_location=="bottom":
                        enemy.attack_location="middle"
                enemy.attacking=True
            
                
                
        if at_panel==True:
            password_progress_text=keypad_display_font.render(password_progress, True, (255,255,255))
                       
            background.blit(keypad_display, (20, 15))
            background.blit(password_progress_text, (220-password_progress_text.get_size()[0], 50-password_progress_text.get_size()[1]/2))     
            
            background.blit(paper, (-50, 320))
            
            
        for i in door_locations:
            background.blit(door_closing_frames[i[1]], (i[0], 120))
            background.blit(console, (i[0]+60, 240))

            
        player_group.draw(background)
        enemy_group.draw(background)        
    
    m_group.update() 
    screen.blit(background, (0, 0))
    pygame.display.flip()