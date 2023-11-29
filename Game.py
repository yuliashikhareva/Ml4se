import random
import time
from signal import signal, alarm, SIGALRM
from termcolor import colored


size = 16
lives = 3
score = "0"
direct ="N"
posx = 0
posy = 0
prev = "  "
dire = 2

winscore = 70

gx = 2
gy = 1

gameover = False
maze = [[" ","██"*(size)],
        ["█","∙ ","∙ ","∙ ","∙ ","∙ ","██","∙ ","∙ ","∙ ","∙ ","██","∙ ","∙ ","∙ ","∙ ","∙ ","█"],
        ["█","∙ ","██","██","██","∙ ","██","∙ ","██","██","∙ ","██","∙ ","██","██","██","∙ ","█"],
        ["█","∙ ","██","∙ ","∙ ","∙ ","∙ ","∙ ","██","██","∙ ","∙ ","∙ ","∙ ","∙ ","██","∙ ","█"],
        ["█","∙ ","██","∙ ","██","∙ ","██","∙ ","██","██","∙ ","██","∙ ","██","∙ ","██","∙ ","█"],
        ["█","∙ ","∙ ","∙ ","██","∙ ","∙ ","∙ ","∙ ","∙ ","∙ ","∙ ","∙ ","██","∙ ","∙ ","∙ ","█"],
        [" ","██","∙ ","██","██","∙ ","██","██","██","██","██","██","∙ ","██","██","∙ ","██"," "],
        [" "," █","∙ ","∙ ","∙ ","∙ ","██","  ","  ","  ","  ","██","∙ ","∙ ","∙ ","∙ ","█ "," "],
        [" "," █","∙ ","██","██","∙ ","██","  ","  ","  ","  ","██","∙ ","██","██","∙ ","█ "," "],
        [" ","██","∙ ","██","∙ ","∙ ","██","██","  ","  ","██","██","∙ ","∙ ","██","∙ ","██"," "],
        ["█","∙ ","∙ ","∙ ","∙ ","∙ ","∙ ","∙ ","∙ ","∙ ","∙ ","∙ ","∙ ","∙ ","∙ ","∙ ","∙ ","█"],
        ["█","∙ ","██","∙ ","██","██","∙ ","██","∙ ","∙ ","██","∙ ","██","██","∙ ","██","∙ ","█"],
        ["█","∙ ","██","∙ ","██","∙ ","∙ ","██","∙ ","∙ ","██","∙ ","∙ ","██","∙ ","██","∙ ","█"],
        ["█","∙ ","██","∙ ","██","∙ ","██","██","██","██","██","██","∙ ","██","∙ ","██","∙ ","█"],
        ["█","∙ ","∙ ","∙ ","██","∙ ","∙ ","∙ ","∙ ","∙ ","∙ ","∙ ","∙ ","██","∙ ","∙ ","∙ ","█"],
        [" ","██"*(size)],
        ]

def game_space ():
    
    print((" "*int(size/2-1)),"Martin's - PacMan")
    print((" "*int(size/1.3)),"Score",score)
    print((" "*int(size-2)),(str(lives)+" ❤"))
    
    for x in range(len(maze)):
     for y in range(len(maze[x])):
         if(maze[x][y] == "▶ " or maze[x][y] == "◀ " or maze[x][y] == "▲ " or maze[x][y] == "▼ "):
             print(colored(maze[x][y],"yellow"),end="")
         elif(maze[x][y]=="∙ "):
             print(maze[x][y],end="")
         elif(maze[x][y]=="◓ "):
             print(colored(maze[x][y],"red"),end="")
              
         else:
             print(maze[x][y],end="")
     print()
     

def ghost_ai():
    global maze,gx,gy,gameover,prev,dire
    running = True
    while running:
        
        if(dire == 0):
            if(maze[gx][gy+1]  == "  " or maze[gx][gy+1]== "∙ "):
                
                maze[gx][gy] = prev
                prev = maze[gx][gy+1]
                maze[gx][gy+1] = "◓ "
                gy+=1
                running = False
                break   
                
        elif(dire == 1):
            if(maze[gx][gy-1]  == "  " or maze[gx][gy-1]== "∙ "):
                
                maze[gx][gy] = prev
                prev = maze[gx][gy-1]
                maze[gx][gy-1] = "◓ "
                gy-=1
                running = False
                break
   


            
