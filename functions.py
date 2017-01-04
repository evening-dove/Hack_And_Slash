import random

def make_passwords(doors_opened, difficulty):
    '''
    make_passwords(int, int) --> String
    Creats a password that the player will need to type in. Takes 2 ints as an
    argument. The first int refers to how many doors the player has opened so
    far. The second int refers to what difficulty level the player is playing
    on. This function returns a String of random characters. The length of the
    return value, and what characters ir contains is determined by the 2 
    arguments.
    '''
    numbers="1234567890"
    letters="qwertyuiopasdfghjklzxcvbnm"
    c_letters="QWERTYUIOPASDFGHJKLZXCVBNM"
    
    password=""
    if difficulty==0:
        for i in range(0, min(9, (int(doors_opened/2))+3)):
            password+=numbers[random.randrange(0,10)]
            
    if difficulty==1:
        for i in range(0, min(9, (int(doors_opened/2))+3)):
            password+=letters[random.randrange(0,26)]
            
    if difficulty==2:
        for i in range(0, min(9, (int(doors_opened/2))+3)):
            password+=str(letters+numbers)[random.randrange(0,36)]
            
    if difficulty==3:
        for i in range(0, min(9, (int(doors_opened/2))+3)):
            password+=str(letters+numbers+c_letters)[random.randrange(0,62)]
            
    return password