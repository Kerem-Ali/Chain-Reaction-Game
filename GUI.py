import pygame,sys
from board import *


myboard=Board(6,10)

BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
BLUE=(0,0,255)

BOX_WIDTH = 50
BOX_HEIGHT = 50
BOX_MARGIN = 5

pygame.init()
window_size=[500,600]
scr=pygame.display.set_mode(window_size)
pygame.display.set_caption("Chain Reaction")


def draw_atom(y,x,color):

    cell=x
    line=y

    num=myboard.board[y][x]

    if num==0:
        return 0
    elif num==1:
        pygame.draw.circle(scr,color,
                                   ((BOX_MARGIN+BOX_WIDTH)*cell+BOX_MARGIN+BOX_WIDTH//2,
                                    (BOX_MARGIN+BOX_HEIGHT)*line+BOX_MARGIN+BOX_HEIGHT//2),5)
        
    elif num==2:
        pygame.draw.circle(scr,color,
                               ((BOX_MARGIN+BOX_WIDTH)*cell+BOX_MARGIN+BOX_WIDTH//2-10,
                                (BOX_MARGIN+BOX_HEIGHT)*line+BOX_MARGIN+BOX_HEIGHT//2),5)

        pygame.draw.circle(scr,color,
                               ((BOX_MARGIN+BOX_WIDTH)*cell+BOX_MARGIN+BOX_WIDTH//2+10,
                                (BOX_MARGIN+BOX_HEIGHT)*line+BOX_MARGIN+BOX_HEIGHT//2),5)
    elif num==3:
       pygame.draw.circle(scr,color,
                               ((BOX_MARGIN+BOX_WIDTH)*cell+BOX_MARGIN+BOX_WIDTH//2-15,
                                (BOX_MARGIN+BOX_HEIGHT)*line+BOX_MARGIN+BOX_HEIGHT//2+10),5)

       pygame.draw.circle(scr,color,
                               ((BOX_MARGIN+BOX_WIDTH)*cell+BOX_MARGIN+BOX_WIDTH//2+15,
                                (BOX_MARGIN+BOX_HEIGHT)*line+BOX_MARGIN+BOX_HEIGHT//2+10),5)

       pygame.draw.circle(scr,color,
                                   ((BOX_MARGIN+BOX_WIDTH)*cell+BOX_MARGIN+BOX_WIDTH//2,
                                    (BOX_MARGIN+BOX_HEIGHT)*line+BOX_MARGIN+BOX_HEIGHT//2-10),5)

    

    

    



done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        elif event.type==pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            column=pos[0]//(BOX_WIDTH+BOX_MARGIN)
            row=pos[1]//(BOX_HEIGHT+BOX_MARGIN)
            if myboard.ispossible(column,row):
                myboard.make_move(column,row)
                myboard.printboard()

            if len(myboard.hamleler)>2:
                wstate=myboard.check_win()
                if wstate!="Continue":
                    print(f"{wstate} kazandi")
            

    scr.fill(BLACK)
    for a,line in enumerate(myboard.board):
        for b,cell in enumerate(line):
            color=WHITE
            pygame.draw.rect(scr,color,
                             [(BOX_MARGIN+BOX_WIDTH)*b+BOX_MARGIN,
                             (BOX_MARGIN+BOX_HEIGHT)*a+BOX_MARGIN,
                             BOX_WIDTH,
                             BOX_HEIGHT])
            if myboard.renkBoard[a][b]=="A":
                color=RED
            elif myboard.renkBoard[a][b]=="B":
                color=BLUE
            draw_atom(a,b,color)
    

    pygame.display.update()

pygame.quit()
            
