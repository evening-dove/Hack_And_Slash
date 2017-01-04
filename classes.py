import pygame
from pygame.locals import *
pygame.init()

import random
import os



class Mouse(pygame.sprite.Sprite):
    def __init__(self):
        '''
        M.__init__()
        Initializes Mouse
        '''
        pygame.sprite.Sprite.__init__(self)
        self.x=0
        self.y=0
        self.last_xs=[0,0,0,0,0,0,0,0,0,0]
        self.last_ys=[0,0,0,0,0,0,0,0,0,0]
        self.image=pygame.Surface((1,1)).convert()
        self.image.fill((0,0,0))
        self.image.set_alpha(0)        
        self.rect=self.image.get_rect()
        
    def update(self):
        '''
        M.update() --> None
        This method is used to move this sprite around on screen, and track the
        mouse.
        '''
        self.last_xs=self.last_xs[1:]+[self.x]
        self.last_ys=self.last_ys[1:]+[self.y]
        
        self.rect.left=self.x
        self.rect.top=self.y
        
        

class Player(pygame.sprite.Sprite):
    def __init__(self, img_dirr):
        '''
        P.__init__(String)
        Initializes Player.
        The character which the player controls.
        Takes as a peramater a string, which is a path from the current working
        dirrectory, to the dirrectory of the images that will be used for this
        object's sprite.
        '''
        pygame.sprite.Sprite.__init__(self)
        
        
        os.chdir(img_dirr+"/main_character")
        
        #Gets the images for the walking animation
        self.walking_frames=[]
        for i in range(1,5):
            temp_frame=pygame.image.load("walking_frame_{}.bmp".format(i)).convert()
            temp_frame.set_colorkey((255,0,255))
            temp_frame=pygame.transform.scale(temp_frame, (int(temp_frame.get_size()[0]*4), int(temp_frame.get_size()[1]*4)))
            self.walking_frames+=[temp_frame]
            
        self.parry_top_frame=pygame.image.load("parry_top.bmp").convert()
        self.parry_top_frame.set_colorkey((255,0,255))
        self.parry_top_frame=pygame.transform.scale(self.parry_top_frame, (int(self.parry_top_frame.get_size()[0]*4), int(self.parry_top_frame.get_size()[1]*4)))
        self.parry_middle_frame=pygame.image.load("parry_middle.bmp").convert()
        self.parry_middle_frame.set_colorkey((255,0,255))
        self.parry_middle_frame=pygame.transform.scale(self.parry_middle_frame, (int(self.parry_middle_frame.get_size()[0]*4), int(self.parry_middle_frame.get_size()[1]*4)))
        self.parry_bottom_frame=pygame.image.load("parry_bottom.bmp").convert()
        self.parry_bottom_frame.set_colorkey((255,0,255))
        self.parry_bottom_frame=pygame.transform.scale(self.parry_bottom_frame, (int(self.parry_bottom_frame.get_size()[0]*4), int(self.parry_bottom_frame.get_size()[1]*4)))
        
        self.walking_counter=0
        self.parry_location="middle"
        self.block_counter=30
        
        self.image=self.parry_middle_frame
        self.rect=self.image.get_rect()
        
        self.rect.bottom=300
        self.rect.left=300
        
        self.doors_opened=0
        self.attacks_blocked=0
        self.wrong_key_penalty=0
        
        
        
        
    def update(self, at_panel):
        '''
        P.update(Bool) --> None
        This method is used to move the player, and update their image.
        As an argument, this method takes a Boolean, which is True if the player
        is currently at a control Pannel, and False if they are not.
        '''
        
        if at_panel==True:
            if self.parry_location=="top":
                self.image=self.parry_top_frame
            if self.parry_location=="middle":
                self.image=self.parry_middle_frame
            if self.parry_location=="bottom":
                self.image=self.parry_bottom_frame
                
                
        if at_panel==False:
            self.image=self.walking_frames[int(self.walking_counter)]
            self.walking_counter+=.25
            if int(self.walking_counter)==4:
                self.walking_counter=0  
                
                
                
                
                

class Enemy(pygame.sprite.Sprite):
    def __init__(self, img_dirr):
        '''
        E.__init__(String)
        Initializes Enemy.
        The enemy which chases the player.
        Takes as a peramater a string, which is a path from the current working
        dirrectory, to the dirrectory of the images that will be used for this
        object's sprite.
        '''
        pygame.sprite.Sprite.__init__(self)
        
        os.chdir(img_dirr+"/enemy")
        
        
        self.walking_frames=[]
        for i in range(1,5):
            temp_frame=pygame.image.load("walking_frame_{}.bmp".format(i)).convert()
            temp_frame.set_colorkey((255,0,255))
            temp_frame=pygame.transform.scale(temp_frame, (int(temp_frame.get_size()[0]*4), int(temp_frame.get_size()[1]*4)))
            self.walking_frames+=[temp_frame]
            
            
        self.idle_frame=pygame.image.load("walking_frame_1.bmp").convert()
        self.idle_frame.set_colorkey((255,0,255))
        self.idle_frame=pygame.transform.scale(self.idle_frame, (int(self.idle_frame.get_size()[0]*4), int(self.idle_frame.get_size()[1]*4)))
            
        self.attack_top_frame=pygame.image.load("attack_top.bmp").convert()
        self.attack_top_frame.set_colorkey((255,0,255))
        self.attack_top_frame=pygame.transform.scale(self.attack_top_frame, (int(self.attack_top_frame.get_size()[0]*4), int(self.attack_top_frame.get_size()[1]*4)))
        self.attack_middle_frame=pygame.image.load("attack_middle.bmp").convert()
        self.attack_middle_frame.set_colorkey((255,0,255))
        self.attack_middle_frame=pygame.transform.scale(self.attack_middle_frame, (int(self.attack_middle_frame.get_size()[0]*4), int(self.attack_middle_frame.get_size()[1]*4)))
        self.attack_bottom_frame=pygame.image.load("attack_bottom.bmp").convert()
        self.attack_bottom_frame.set_colorkey((255,0,255))
        self.attack_bottom_frame=pygame.transform.scale(self.attack_bottom_frame, (int(self.attack_bottom_frame.get_size()[0]*4), int(self.attack_bottom_frame.get_size()[1]*4)))
        
        self.walking_counter=0
        self.attack_location="none"
        
        self.attack_counter=10
        self.attacking=False
        
        self.image=self.attack_middle_frame
        self.rect=self.image.get_rect()
        
        self.rect.bottom=300
        self.rect.left=380
        
        
    def update(self, at_panel):
        '''
        E.update(Bool) --> None
        This method is used to move the enemy, and update their image.
        As an argument, this method takes a Boolean, which is True if the player
        character is currently at a control Pannel, and False if they are not.
        '''
        
        if at_panel==True:
            if self.attack_location=="none":
                self.image=self.idle_frame
            if self.attack_location=="top":
                self.image=self.attack_top_frame
            if self.attack_location=="middle":
                self.image=self.attack_middle_frame
            if self.attack_location=="bottom":
                self.image=self.attack_bottom_frame
                
                
        if at_panel==False:
            self.image=self.walking_frames[int(self.walking_counter)]
            self.walking_counter+=.25
            if int(self.walking_counter)==4:
                self.walking_counter=0