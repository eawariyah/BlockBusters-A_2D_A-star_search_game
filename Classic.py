"""
Created on 12 Nov 2022

@authors: Edwin, Kwaku
""" 

import pygame_menu
from pygame import*
from random import randint
import pygame
from numpy import sqrt
import time 
import turtle


pygame.init()
surface = pygame.display.set_mode((600, 600))


def set_difficulty(valuex, otherx):#difficulty choice
    global tx
    u,v=valuex
    a,b=u
    tx = a
    
def control_choice(valuey, othery):#control choice 
    global ty
    u,v=valuey
    a,b=u
    ty = a
def competitive_choice(valuez, otherz):#competitive choice
    global tz
    u,v=valuez
    a,b=u
    tz = a

def start_the_game():
    print(tx)#difficulty 
    print(ty)#control method
    print(tz)#competitive mode
    start = time.time()

    
    init()#to initialize music
    pygame.mixer.init()#to initialize music

    
    pygame.mixer.music.load("9convert.com - Scott Joplin The Entertainer Paul Barton FEURICH HP piano.mp3")
    pygame.mixer.music.play(-1)
        
    sound_effect1 = pygame.mixer.Sound("CymbalCrash CRT043807.mp3")
    sound_effect2 = pygame.mixer.Sound("8d82b5_Pacman_Eating_Cherry_Sound_Effect.mp3")
    #sound_effect1.set_volume(0.1)
    #sound_effect2.set_volume(0.1)




    print("\nYou may need to minimize your IDE to see the actions")
    choice_difficulty_level = tx
    choice_input = ty
    competitive_mode = tz      
    
    
    if choice_difficulty_level == 'Easy':
        speed_value = 10
        obstacle_frequency = 5
    elif choice_difficulty_level == 'Medium':
        speed_value = 25
        obstacle_frequency = 10
    elif choice_difficulty_level == 'Hard':
        speed_value = 30
        obstacle_frequency = 15
    else:
        speed_value = 35
        obstacle_frequency = 15
    
    
    done = False
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    WHITE = (255, 255, 255)
    cols = 50#colums
    rows = 50#rows
    counter = 0
    value = 0
    
    
    width = 600#widdth
    height = 600#height
    wr = width/cols
    hr = height/rows
    direction = 1 #initial starting direction - right
    
    screen = display.set_mode([width, height])
    display.set_caption("Search star")
    clock = pygame.time.Clock()
    
    
    def getpath(goal_state1, a_star1):
        goal_state1.camefrom = []#new empty list camefrom from goal_state1
        for s in a_star1:
            s.camefrom = []#for each value in a_star1 make a new list from it
        openset = [a_star1[-1]]#the last value of a_star1
        closedset = []#new empty list called closedset
        dir_array1 = []#new empty list called dir_array1
        while 1:#while true
            current1 = min(openset, key=lambda x: x.f)#takes the index of an item f in list x, sets that as the key
            # print(current1)
            # current1 = min(openset, key=lambda x: x.g)#takes the index of an item f in list x, sets that as the key

            openset = [openset[i] for i in range(len(openset)) if not openset[i] == current1]
            closedset.append(current1)
            for neighbor in current1.neighbors:
                if neighbor not in closedset and not neighbor.block and neighbor not in a_star1:
                    tempg = neighbor.g + 1
                    if neighbor in openset:
                        if tempg < neighbor.g:
                            neighbor.g = tempg
                    else:
                        neighbor.g = tempg
                        openset.append(neighbor)
                    neighbor.h = sqrt((neighbor.x - goal_state1.x) ** 2 + (neighbor.y - goal_state1.y) ** 2)
                    neighbor.f = neighbor.g + neighbor.h
                    neighbor.camefrom = current1
            if current1 == goal_state1:
                break
        while current1.camefrom:
            if current1.x == current1.camefrom.x and current1.y < current1.camefrom.y:
                dir_array1.append(2)
            elif current1.x == current1.camefrom.x and current1.y > current1.camefrom.y:
                dir_array1.append(0)
            elif current1.x < current1.camefrom.x and current1.y == current1.camefrom.y:
                dir_array1.append(3)
            elif current1.x > current1.camefrom.x and current1.y == current1.camefrom.y:
                dir_array1.append(1)
            current1 = current1.camefrom
        for i in range(rows):
            for j in range(cols):
                grid[i][j].camefrom = []
                grid[i][j].f = 0
                grid[i][j].h = 0
                grid[i][j].g = 0
        return dir_array1
    
    
    class Spot:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.f = 0
            self.g = 0
            self.h = 0
            self.neighbors = []
            self.camefrom = []
            self.block = False
            
            if competitive_mode == 'No':
            
                rad = randint(1, 101)        
            
                if rad < obstacle_frequency: #obstacle randomness
                    self.block = True
    
    
    
        def show(self, color):
            draw.rect(screen, color, [self.x*hr+2, self.y*wr+2, hr-4, wr-4])
            
        def show1(self, color):
            draw.rect(screen, color, [self.x*hr+2, self.y*wr+2, hr-4, wr-4], 10, 90)
    
        def add_neighbors(self):
            if self.x > 0:
                self.neighbors.append(grid[self.x - 1][self.y])
            if self.y > 0:
                self.neighbors.append(grid[self.x][self.y - 1])
            if self.x < rows - 1:
                self.neighbors.append(grid[self.x + 1][self.y])
            if self.y < cols - 1:
                self.neighbors.append(grid[self.x][self.y + 1])
    
    grid = [[Spot(i, j) for j in range(cols)] for i in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            grid[i][j].add_neighbors()
    
    for m in range(rows):
        grid[m][49].block = True #bottom row as blocks
        grid[m][49].show(WHITE)
    for m in range(rows):
        grid[m][0].block = True #top row as blocks
        grid[m][0].show(WHITE)
    for m in range(cols):
        grid[0][m].block = True #leftmost column as blocks
        grid[0][m].show(WHITE)
    for m in range(cols):
        grid[49][m].block = True #rightmost column as block
        grid[49][m].show(WHITE) 
    
    #===============================================================================
    # Predefined for competitive_mode
    #===============================================================================
    if competitive_mode == 'Yes': 
        #===============================================================================
        # Column 1        
        #===============================================================================
        grid[1][17].block = True #bottom row as blocks
        grid[1][17].show(WHITE)
        
        grid[1][33].block = True #bottom row as blocks
        grid[1][33].show(WHITE)
        #==============================================================================
        # Column 2       
        #==============================================================================
        grid[2][33].block = True #bottom row as blocks
        grid[2][33].show(WHITE)
        
        grid[2][15].block = True #bottom row as blocks
        grid[2][15].show(WHITE)
        #===============================================================================
        # Column 3
        #===============================================================================
        grid[3][24].block = True #bottom row as blocks
        grid[3][24].show(WHITE)
        
        grid[3][30].block = True #bottom row as blocks
        grid[3][30].show(WHITE)
        #===============================================================================
        # Column 4
        #===============================================================================
        grid[4][35].block = True #bottom row as blocks
        grid[4][35].show(WHITE)
        
        grid[4][43].block = True #bottom row as blocks
        grid[4][43].show(WHITE)
        #===============================================================================
        # Column 5
        #===============================================================================
        grid[5][17].block = True #bottom row as blocks
        grid[5][17].show(WHITE)
        
        grid[5][33].block = True #bottom row as blocks
        grid[5][33].show(WHITE)
        #===============================================================================
        # Column 6
        #===============================================================================
        grid[6][28].block = True #bottom row as blocks
        grid[6][28].show(WHITE)
        
        grid[6][6].block = True #bottom row as blocks
        grid[6][6].show(WHITE)
        #===============================================================================
        # Column 7
        #===============================================================================
        grid[7][39].block = True #bottom row as blocks
        grid[7][39].show(WHITE)
        
        grid[7][24].block = True #bottom row as blocks
        grid[7][24].show(WHITE)
        #===============================================================================
        # Column 8
        #===============================================================================
        grid[8][11].block = True #bottom row as blocks
        grid[8][11].show(WHITE)
        
        grid[8][25].block = True #bottom row as blocks
        grid[8][25].show(WHITE)
        #===============================================================================
        # Column 9
        #===============================================================================
        grid[9][38].block = True #bottom row as blocks
        grid[9][38].show(WHITE)
        
        grid[9][5].block = True #bottom row as blocks
        grid[9][5].show(WHITE)
        #===============================================================================
        # Column 10
        #===============================================================================
        grid[10][6].block = True #bottom row as blocks
        grid[10][6].show(WHITE)
        
        grid[10][15].block = True #bottom row as blocks
        grid[10][15].show(WHITE)
        #===============================================================================
        # Column 11
        #===============================================================================
        grid[11][8].block = True #bottom row as blocks
        grid[11][8].show(WHITE)
        
        grid[11][12].block = True #bottom row as blocks
        grid[11][12].show(WHITE)
        #===============================================================================
        # Column 12
        #===============================================================================
        grid[12][30].block = True #bottom row as blocks
        grid[12][30].show(WHITE)
        
        grid[12][11].block = True #bottom row as blocks
        grid[12][11].show(WHITE)
        #===============================================================================
        # Column 13
        #===============================================================================
        grid[13][20].block = True #bottom row as blocks
        grid[13][20].show(WHITE)
        
        grid[13][32].block = True #bottom row as blocks
        grid[13][32].show(WHITE)
        #===============================================================================
        # Column 14
        #===============================================================================
        grid[14][30].block = True #bottom row as blocks
        grid[14][30].show(WHITE)
        
        grid[14][44].block = True #bottom row as blocks
        grid[14][44].show(WHITE)
        #===============================================================================
        # Column 15
        #===============================================================================
        grid[15][41].block = True #bottom row as blocks
        grid[15][41].show(WHITE)
        
        grid[15][23].block = True #bottom row as blocks
        grid[15][23].show(WHITE)
        #===============================================================================
        # Column 16
        #===============================================================================
        grid[16][32].block = True #bottom row as blocks
        grid[16][32].show(WHITE)
        
        grid[16][25].block = True #bottom row as blocks
        grid[16][25].show(WHITE)
        #===============================================================================
        # Column 17
        #===============================================================================
        grid[17][7].block = True #bottom row as blocks
        grid[17][7].show(WHITE)
        
        grid[17][46].block = True #bottom row as blocks
        grid[17][46].show(WHITE)
        #===============================================================================
        # Column 18
        #===============================================================================
        grid[18][45].block = True #bottom row as blocks
        grid[18][45].show(WHITE)
        
        grid[18][24].block = True #bottom row as blocks
        grid[18][24].show(WHITE)
        #===============================================================================
        # Column 19
        #===============================================================================
        grid[19][9].block = True #bottom row as blocks
        grid[19][9].show(WHITE)
        
        grid[19][42].block = True #bottom row as blocks
        grid[19][42].show(WHITE)
        #===============================================================================
        # Column 20
        #===============================================================================
        grid[20][15].block = True #bottom row as blocks
        grid[20][15].show(WHITE)
        
        grid[20][16].block = True #bottom row as blocks
        grid[20][16].show(WHITE)
        #===============================================================================
        # Column 21
        #===============================================================================
        grid[21][24].block = True #bottom row as blocks
        grid[21][24].show(WHITE)
        
        grid[21][19].block = True #bottom row as blocks
        grid[21][19].show(WHITE)
        #===============================================================================
        # Column 22
        #===============================================================================
        grid[22][32].block = True #bottom row as blocks
        grid[22][32].show(WHITE)
        
        grid[22][13].block = True #bottom row as blocks
        grid[22][13].show(WHITE)
        #===============================================================================
        # Column 23
        #===============================================================================
        grid[23][48].block = True #bottom row as blocks
        grid[23][48].show(WHITE)
        
        grid[23][2].block = True #bottom row as blocks
        grid[23][2].show(WHITE)
        #===============================================================================
        # Column 24
        #===============================================================================
        grid[24][2].block = True #bottom row as blocks
        grid[24][2].show(WHITE)
        
        grid[24][20].block = True #bottom row as blocks
        grid[24][20].show(WHITE)
        #===============================================================================
        # Column 25
        #===============================================================================
        grid[25][2].block = True #bottom row as blocks
        grid[25][2].show(WHITE)
        
        grid[25][8].block = True #bottom row as blocks
        grid[25][8].show(WHITE)
        #===============================================================================
        # Column 26
        #===============================================================================
        grid[26][44].block = True #bottom row as blocks
        grid[26][44].show(WHITE)
        
        grid[26][3].block = True #bottom row as blocks
        grid[26][3].show(WHITE)
        #===============================================================================
        # Column 27
        #===============================================================================
        grid[27][13].block = True #bottom row as blocks
        grid[27][13].show(WHITE)
        
        grid[27][40].block = True #bottom row as blocks
        grid[27][40].show(WHITE)
        #===============================================================================
        # Column 28
        #===============================================================================
        grid[28][42].block = True #bottom row as blocks
        grid[28][42].show(WHITE)
        
        grid[28][8].block = True #bottom row as blocks
        grid[28][8].show(WHITE)
        #===============================================================================
        # Column 29
        #===============================================================================
        grid[29][8].block = True #bottom row as blocks
        grid[29][8].show(WHITE)
        
        grid[29][38].block = True #bottom row as blocks
        grid[29][38].show(WHITE)
        #===============================================================================
        # Column 30
        #===============================================================================
        grid[30][32].block = True #bottom row as blocks
        grid[30][32].show(WHITE)
        
        grid[30][29].block = True #bottom row as blocks
        grid[30][29].show(WHITE)
        #===============================================================================
        # Column 31
        #===============================================================================
        grid[31][42].block = True #bottom row as blocks
        grid[31][42].show(WHITE)
        
        grid[31][21].block = True #bottom row as blocks
        grid[31][21].show(WHITE)
        #===============================================================================
        # Column 32
        #===============================================================================
        grid[32][48].block = True #bottom row as blocks
        grid[32][48].show(WHITE)
        
        grid[32][18].block = True #bottom row as blocks
        grid[32][18].show(WHITE)
        #===============================================================================
        # Column 33
        #===============================================================================
        grid[33][20].block = True #bottom row as blocks
        grid[33][20].show(WHITE)
        
        grid[33][10].block = True #bottom row as blocks
        grid[33][10].show(WHITE)
        #===============================================================================
        # Column 34
        #===============================================================================
        grid[34][7].block = True #bottom row as blocks
        grid[24][7].show(WHITE)
        
        grid[34][41].block = True #bottom row as blocks
        grid[24][41].show(WHITE)
        #===============================================================================
        # Column 35
        #===============================================================================
        grid[35][18].block = True #bottom row as blocks
        grid[35][18].show(WHITE)
        
        grid[35][19].block = True #bottom row as blocks
        grid[35][19].show(WHITE)
        #===============================================================================
        # Column 36
        #===============================================================================
        grid[36][34].block = True #bottom row as blocks
        grid[36][34].show(WHITE)
        
        grid[36][36].block = True #bottom row as blocks
        grid[36][36].show(WHITE)
        #===============================================================================
        # Column 37
        #===============================================================================
        grid[37][24].block = True #bottom row as blocks
        grid[37][24].show(WHITE)
        
        grid[37][3].block = True #bottom row as blocks
        grid[37][3].show(WHITE)
        #===============================================================================
        # Column 38
        #===============================================================================
        grid[38][26].block = True #bottom row as blocks
        grid[38][26].show(WHITE)
        
        grid[38][41].block = True #bottom row as blocks
        grid[38][41].show(WHITE)
        #===============================================================================
        # Column 39
        #===============================================================================
        grid[39][27].block = True #bottom row as blocks
        grid[39][27].show(WHITE)
        
        grid[39][26].block = True #bottom row as blocks
        grid[39][26].show(WHITE)
        #===============================================================================
        # Column 40
        #===============================================================================
        grid[40][26].block = True #bottom row as blocks
        grid[40][26].show(WHITE)
        
        grid[40][46].block = True #bottom row as blocks
        grid[40][46].show(WHITE)
        #===============================================================================
        # Column 41
        #===============================================================================
        grid[41][37].block = True #bottom row as blocks
        grid[41][37].show(WHITE)
        
        grid[41][7].block = True #bottom row as blocks
        grid[41][7].show(WHITE)
        #===============================================================================
        # Column 42
        #===============================================================================
        grid[42][48].block = True #bottom row as blocks
        grid[42][48].show(WHITE)
        
        grid[42][9].block = True #bottom row as blocks
        grid[42][9].show(WHITE)
        #===============================================================================
        # Column 43
        #===============================================================================
        grid[43][48].block = True #bottom row as blocks
        grid[43][48].show(WHITE)
        
        grid[43][8].block = True #bottom row as blocks
        grid[43][8].show(WHITE)
        #===============================================================================
        # Column 44
        #===============================================================================
        grid[44][18].block = True #bottom row as blocks
        grid[44][18].show(WHITE)
        
        grid[44][37].block = True #bottom row as blocks
        grid[44][37].show(WHITE)
        #===============================================================================
        # Column 45
        #===============================================================================
        grid[45][18].block = True #bottom row as blocks
        grid[45][18].show(WHITE)
        
        grid[45][5].block = True #bottom row as blocks
        grid[45][5].show(WHITE)
        #===============================================================================
        # Column 46
        #===============================================================================
        grid[46][42].block = True #bottom row as blocks
        grid[46][42].show(WHITE)
        
        grid[46][27].block = True #bottom row as blocks
        grid[46][27].show(WHITE)
        #===============================================================================
        # Column 47
        #===============================================================================
        grid[47][33].block = True #bottom row as blocks
        grid[47][33].show(WHITE)
        
        grid[47][6].block = True #bottom row as blocks
        grid[47][6].show(WHITE)
        #===============================================================================
        # Column 48
        #===============================================================================
        grid[48][10].block = True #bottom row as blocks
        grid[48][10].show(WHITE)
        
        grid[48][28].block = True #bottom row as blocks
        grid[48][28].show(WHITE)
    
    
    a_star = [grid[round(rows/2)][round(cols/2)]]
    # goal_state = grid[randint(3, rows-3)][randint(3, cols-3)]# initial goal state initial randomness
    goal_state = grid[(7)][(10)]#goal state randomness
    
    current = a_star[-1]
    dir_array = getpath(goal_state, a_star)
    goal_state_array = [goal_state]
    
    
    
    
    while not done:
        clock.tick(speed_value)
        
        screen.fill(BLACK)
            
        if choice_input == 'User':    
        #===========================================================================
        # Taking keyboard movement
        #===========================================================================
        
            key = pygame.key.get_pressed()
            if key[pygame.K_DOWN]: #Keyboard press down
                direction = 0 #go down
            if current.y == 48:#Hitting the bottom wall
                direction = 2#Go up 
            if ((grid[current.x][current.y+1].block) == True):#Hitting an obstacle going up
                direction = 2
                sound_effect1.play()
            if key[pygame.K_UP]: #keyboard press up
                direction = 2 #go up
            if current.y == 1:#Hitting the top wall
                direction = 0#go down
            if ((grid[current.x][current.y-1].block) == True):#Hitting an obstacle going up
                direction = 0#go down
                sound_effect1.play()
            if key[pygame.K_LEFT]:#keyboard press left
                direction = 3 #go left
            if current.x == 1:#Hitting the left wall
                direction = 1#Go right
            if ((grid[current.x-1][current.y].block) == True):#Hitting an obstacle going right
                direction = 1#Go left
                sound_effect1.play()
            if key[pygame.K_RIGHT]:#Keyboard press right
                direction = 1 #go right
            if current.x == 48:#Hitting the right wall
                direction = 3#go left
            if ((grid[current.x+1][current.y].block) == True):#Hitting an obstacle going right
                direction = 3#Go left
                sound_effect1.play()
            if ((grid[current.x+1][current.y].block) == True and (grid[current.x-2][current.y].block) == True and key[pygame.K_UP]): #If player gets stuck between left and right obstacles surrounding it and user presses up
                direction = 2#go up
                # sound_effect1.play()
            if ((grid[current.x+1][current.y].block) == True and (grid[current.x-2][current.y].block) == True and key[pygame.K_DOWN]): #If player gets stuck between left and right obstacles surrounding it and user presses down
                direction = 0#go down
                # sound_effect1.play()
            if ((grid[current.x][current.y+1].block) == True and (grid[current.x][current.y-2].block) == True and key[pygame.K_RIGHT]): #If player gets stuck between left and right obstacles surrounding it and user presses up
                direction = 1#go right
                # sound_effect1.play()
            if ((grid[current.x][current.y+1].block) == True and (grid[current.x][current.y-2].block) == True and key[pygame.K_LEFT]): #If player gets stuck between left and right obstacles surrounding it and user presses down
                direction = 3#go left
                # sound_effect1.play()
                
                
            if (((grid[current.x-1][current.y].block) == True and (grid[current.x+1][current.y].block) == True) and key[pygame.K_UP]):
                direction = 2 #go up
                # sound_effect1.play()
            if (((grid[current.x-1][current.y].block) == True and (grid[current.x+1][current.y].block) == True) and key[pygame.K_DOWN]):
                direction = 0#go down
                # sound_effect1.play()
            if (((grid[current.x][current.y-1].block) == True and (grid[current.x][current.y+1].block) == True) and key[pygame.K_LEFT]):
                direction = 3#go left
                # sound_effect1.play()
            if (((grid[current.x][current.y-1].block) == True and (grid[current.x][current.y+1].block) == True) and key[pygame.K_DOWN]):
                direction = 1#go right
                # sound_effect1.play()
                
            #=======================================================================
            # Left wall    
            #=======================================================================
            if ((current.x - 1 == 1 and grid[current.x+1][current.y].block == True) and key[pygame.K_UP]):
                direction = 2 #go up
            if ((current.x - 1 == 1 and grid[current.x+1][current.y].block == True) and key[pygame.K_DOWN]):
                direction = 0 #go down
            #=======================================================================
            # Right wall  
            #=======================================================================
            if ((current.x + 1  == 48 and grid[current.x-1][current.y].block == True) and key[pygame.K_UP]):
                direction = 2 #go up
            if ((current.x + 1 == 48 and grid[current.x-1][current.y].block == True) and key[pygame.K_DOWN]):
                direction = 0 #go down
                
            #=======================================================================
            # wall left and block right 
            #=======================================================================
            if (current.x == 1 and key[pygame.K_UP] and current.y != 1 and grid[current.x][current.y-1].block != True):
                direction = 2 #go up
            if (current.x == 1 and key[pygame.K_DOWN] and current.y != 48 and grid[current.x][current.y+1].block != True):
                direction = 0#go down        
            #=======================================================================
            # wall right and block left 
            #=======================================================================
            if (current.x == 48 and key[pygame.K_UP] and current.y != 48 and grid[current.x][current.y-1].block != True):
                direction = 2#go up
            if (current.x == 48 and key[pygame.K_DOWN] and current.y != 48 and grid[current.x][current.y+1].block != True):
                direction = 0 #go down
           
        #=======================================================================
        # To use A* Array list
        #=======================================================================
    
        else:
                direction = dir_array.pop(-1)
    
        
        if direction == 0:    # down
            a_star.append(grid[current.x][current.y + 1])
        elif direction == 1:  # right
            a_star.append(grid[current.x + 1][current.y])
        elif direction == 2:  # up
            a_star.append(grid[current.x][current.y - 1])
        elif direction == 3:  # left
            a_star.append(grid[current.x - 1][current.y])
        current = a_star[-1]
        # print(grid[current.x][current.y].block)
        
        if current.x == goal_state.x and current.y == goal_state.y:
            counter += 1
            value += 1
            sound_effect2.play()

            while 1:
                #===================================================================
                # predefined for competitive mode
                #===================================================================
                if competitive_mode == 'Yes':
                    if value == 1:
                        goal_state = grid[31][1]
                    if value == 2:
                        goal_state = grid[23][43]
                    if value == 3:
                        goal_state = grid[32][16]
                    if value == 4:
                        goal_state = grid[48][43]
                    if value == 5:
                        goal_state = grid[45][31]
                    if value == 6:
                        goal_state = grid[32][12]
                    if value == 7:
                        goal_state = grid[36][45]
                    if value == 8:
                        goal_state = grid[20][9]
                    if value == 9:
                        goal_state = grid[30][23]
                    if value == 10:
                        goal_state = grid[18][4]
                    if value == 11:
                        goal_state = grid[23][34]
                    if value == 12:
                        goal_state = grid[27][10]
                    if value == 13:
                        goal_state = grid[1][24]
                    if value == 14:
                        goal_state = grid[32][40]
                    if value == 15:
                        goal_state = grid[30][26]
                    if value == 16:
                        goal_state = grid[38][47]
                    if value == 17:
                        goal_state = grid[2][29]
                    if value == 18:
                        goal_state = grid[6][30]
                    if value == 19:
                        goal_state = grid[47][40]
                    if value == 20:
                        goal_state = grid[13][36]
                    if value == 21:
                        goal_state = grid[41][27]
                    if value == 22:
                        goal_state = grid[16][7]
                    if value == 23:
                        goal_state = grid[24][43]
                    if value == 24:
                        goal_state = grid[48][16]
                    if value == 25:
                        goal_state = grid[18][4]
                    if value == 26:
                        goal_state = grid[23][34]
                    if value == 27:
                        goal_state = grid[27][10]
                    if value == 28:
                        goal_state = grid[1][24]
                    if value == 29:
                        goal_state = grid[32][40]
                    if value == 30:
                        goal_state = grid[30][26]
                    if value == 31:
                        goal_state = grid[38][47]
                    if value == 32:
                        goal_state = grid[2][29]
                    if value == 33:
                        goal_state = grid[6][30]
                    if value == 34:
                        goal_state = grid[47][40]
                    if value == 35:
                        goal_state = grid[13][36]
                    if value == 36:
                        goal_state = grid[41][27]
                    if value == 37:
                        goal_state = grid[16][7]
                    if value == 38:
                        goal_state = grid[24][43]
                    if value == 39:
                        goal_state = grid[48][16]
                else:
                    goal_state = grid[randint(3, rows - 3)][randint(3, cols - 3)]
                if not (goal_state.block or goal_state in a_star):
                    break
            goal_state_array.append(goal_state)
            dir_array = getpath(goal_state, a_star)
        else:
            a_star.pop(0)
    
    
    #===============================================================================
    # If block exists for normal mode ie no competitive mode show it
    #===============================================================================
        for i in range(rows):
            for j in range(cols):
                if grid[i][j].block:
                    grid[i][j].show(WHITE)
                    
            
                  
        goal_state.show1(GREEN)#display goal
        a_star[-1].show(BLUE)#display player
    
        end = time.time()#get end time stamp
        timex = int(end - start)#calculate end time
    
        #===========================================================================
        # Display score and time at left and right corners
        #===========================================================================
        font_style = pygame.font.SysFont("bahnschrift", 15)#time font
        
        msg = "Score: " + str(counter)#print score
        mesg = font_style.render(msg, True, RED)
        screen.blit(mesg, [30, 8])#position left
        msg1 = "Time: " + str(timex) + " s"#print time
        mesg1 = font_style.render(msg1, True, RED)
        screen.blit(mesg1, [500, 8])#position right
        
        
                  
    
        display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
                
        if competitive_mode == 'Yes' and str(timex) == '30' and choice_input == 'A* algorithm':
            t = turtle.Turtle()
            t.hideturtle()
            t.goto(0,0)
            t.write("The A* scored " + str(counter) + " in " + str(timex) + "s")
            t.screen.exitonclick()
            pygame.mixer.music.stop()

            
            done = True
        if competitive_mode == 'Yes' and str(timex) == '30' and choice_input == 'User':
            t = turtle.Turtle()
            t.penup()
            t.hideturtle()
            t.goto(-100,0)
            t.write("You scored " + str(counter) + " in " + str(timex) + "s")
            t.goto(-100,100)
            t.write("You can do better \n\tA-star in 'Easy' mode scores at least 8 in 30s\n\tA-star in 'Medium' mode scores at least 20 in 30s\n\tA-star in 'Hard' mode scores at least 24 in 30s\n\tA-star in 'god-mode' mode scores at least 27 in 30s")
            t.screen.exitonclick()
            pygame.mixer.music.stop()
            
            done = True
    

menu = pygame_menu.Menu('Welcome', 600, 600,
                       theme=pygame_menu.themes.THEME_DARK)#menu theme

menu.add.text_input('Name : ', default='Enter name')#default name
menu.add.selector('Difficulty :', [('', 0),('Easy', 1), ('Medium', 2), ('Hard', 3), ('god-mode', 3)], onchange=set_difficulty)
menu.add.selector('Control method :', [('', 0),('A* algorithm', 5), ('User', 6)], onchange=control_choice)
menu.add.selector('Competitive mode :', [('', 0),('Yes', 7), ('No', 8)], onchange=competitive_choice)

menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)    


menu.mainloop(surface)
