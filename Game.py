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
     

        if(maze[x+1][y]=="∙ "):
            maze[x][y] = "▼ "
            direct ="D"
    except:
        print(" ")
    posx = x
    posy = y

def move():
    global direct,maze,posx,posy,score,gameover
    
    x = None
    signal(SIGALRM, lambda x, y: 1/0)
    try:
        
        alarm(1)
        x = str(input(">>>"))
        
  
        if(direct =="R"):
            maze[posx][posy] = "  "
            score = int(score)+1
            posy+=1

            if(maze[posx][posy] == "  " or maze[posx][posy] == "∙ "):
                maze[posx][posy] = "▶ "
            else:
                gameover =True
            running = False
            break




            
