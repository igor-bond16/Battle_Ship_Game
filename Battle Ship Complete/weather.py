import pygame
from pygame.locals import *
import math
import time
import numpy as np
import tkinter as tk
import random

pygame.init()
pygame.font.init()  
win = pygame.display.set_mode((1500,1000))                             

st_list = ("A","B","C","D","E","F","G","H","I","J")
num_list = ("F1","F2","F3","F4","F5","F6","F7","F8","F9","F10")

array_1 = np.zeros([10,10],dtype=int)
array_2 = np.zeros([10,10],dtype=int)
numbers = []
bombed = [i for i in range(100)]
player_1 = True
p1_counter = 0
p2_counter = 0
victory = pygame.mixer.Sound('/home/igor-bond/Downloads/Short_triumphal_fanfare-John_Stracke-815794903.wav')
lose = pygame.mixer.Sound('/home/igor-bond/Downloads/Sad_Trombone-Joe_Lamb-665429450.wav')
failed = pygame.mixer.Sound('/home/igor-bond/Downloads/Video_Game_Splash-Ploor-699235037.wav')
bombed_sound = pygame.mixer.Sound('/home/igor-bond/Downloads/Bomb-SoundBible.com-891110113.wav')
bgm = pygame.mixer.music.load('/home/igor-bond/Downloads/Epic-battle-music-grzegorz-majcherczyk-heroica.mp3')
pygame.mixer.music.play()

def p1_field(win):
    rows = 10
    x = 55
    y = 55
    sizeBwn = 65

    for i in range(rows):
        x += sizeBwn
        y += sizeBwn
        pygame.draw.line(win,(0,0,0),(x,55),(x,705))
        pygame.draw.line(win,(0,0,0),(55,y),(705,y))

        pygame.draw.line(win,(0,0,0),(55,55),(55,705),5)
        pygame.draw.line(win,(0,0,0),(55,55),(705,55),5)
        pygame.draw.line(win,(0,0,0),(55,705),(705,705),5)
        pygame.draw.line(win,(0,0,0),(705,55),(705,705),5)
    
    drawnumbers(87.5,win)
    drawstring(87.5,win)

def p2_field(win):
    rows = 10
    x = 730
    y = 55
    sizeBwn = 65

    for i in range(rows):
        x += sizeBwn
        y += sizeBwn
        pygame.draw.line(win,(0,0,0),(x,55),(x,705))
        pygame.draw.line(win,(0,0,0),(730,y),(1380,y))

        pygame.draw.line(win,(0,0,0),(730,55),(730,705),5)
        pygame.draw.line(win,(0,0,0),(730,55),(1380,55),5)
        pygame.draw.line(win,(0,0,0),(730,705),(1380,705),5)
        pygame.draw.line(win,(0,0,0),(1380,55),(1380,705),5)
    
    drawnumbers(765,win)

def drawnumbers(pos,win):
    for b in num_list:
        font = pygame.font.SysFont('comicsens',25)
        text = font.render(b,1,(0,0,0))
        win.blit(text,(pos - (text.get_width()/2),5))
        pos += 65

def drawstring(pos,win):
    for i in st_list:
        font = pygame.font.SysFont('comicsens',25)
        text = font.render(i,1,(0,0,0))
        win.blit(text,(5,pos - (text.get_width()/2)))
        pos += 65

def settingships():
    column = -1
    row = 0
    root = tk.Tk()
    root.title('numbers')
    root.geometry('470x310')
    for i in range(101):
        if i > 0:
            if i%10 == 1:
                row += 1 
                column = -1
            column += 1
            text=f'{i}'
            btn = tk.Button(root, text=text)
            btn.grid(column=column, row=row)
            btn.config(command=collback(btn,i))  
    root.mainloop()
    main()

def collback(btn,i):
    def nothing():
        btn.config(bg='#008000')
        numbers.append(i)
    return nothing

def draw_ships(array, numbers):
    width = 65
    numbers = np.sort(numbers)
    for i in numbers:
        array.flat[i-1] = 1
    array = array.reshape(-1,1)
    for i in np.where(array == 1)[0]:
        index = i//10
        if i >= 10:
            columns = int(str(i)[1:])
        else:
            columns = i
        pygame.draw.rect(win,(0,0,0),(55+width*columns,55+width*index,width,width),0)
    pygame.display.update()
    ai_ships(array_2)

def ai_ships(array):
    num_5 = random.randint(0,5)
    num_4_1 = random.randint(8,9)
    num_4_2 = random.randint(3,6)
    num_3_1 = random.randint(3,6)
    num_3_2 = random.randint(5,7)
    num_2 = random.randint(2,6)
    num_1_1 = random.randint(0,2)
    num_1_2 = random.randint(5,9)
    if num_5 >= 7:
        array[num_5:num_5+5,0] = 1
    if num_5 <= 6:
        array[-5:,0] = 1
    array[num_3_1,num_3_2:num_3_2+3] = 1
    array[num_2,2:4] = 1
    array[num_4_1,num_4_2:num_4_2+4] = 1
    array[num_1_1,num_1_2] = 1
    array = array.reshape(-1,1)
    pygame.display.update()
    print(array.reshape(10,10))

def bomb_buttons():
    column = -1
    row = 0
    root = tk.Tk()
    root.title('numbers')
    root.geometry('470x310')
    for i in range(101):
        if i > 0:
            if i%10 == 1:
                row += 1 
                column = -1
            column += 1
            text=f'{i}'
            btn = tk.Button(root, text=text)
            btn.grid(column=column, row=row)
            btn.config(command=collback2(btn,i))      
    root.mainloop()

def bombing(i):
    global p1_counter,p2_counter
    font = pygame.font.SysFont('comicsens',100)
    i -= 1
    array = array_2.reshape(-1,1) 
    width = 65  
    index=i//10
    if i >= 10:
        columns = int(str(i)[1:])
    else:
        columns = i
    if array[i] == 1:
        array[i] = 0
        pygame.draw.circle(win,(255,0,0),((730+columns*width)+width//2,(55+index*width)+width//2),width//2,0)
        bombed_sound.play()
        p1_counter += 1
    elif array[i] == 0:
        pygame.draw.circle(win,(0,0,0),((730+columns*width)+width//2,(55+index*width)+width//2),width//2,0)
        failed.play()
    if p1_counter == 15:
        pygame.mixer.music.pause()
        text = font.render('You Win!!',5,(255,0,0))
        win.blit(text,(750-text.get_width()/2,200))
        pygame.display.update()
        victory.play()

    select_num = random.randint(0,99)
    num = bombed[select_num]
    bombed.append(num)
    array1 = array_1.reshape(-1,1)
    while True:
        if num in bombed:
            num = random.randint(0,99)
        else:
            break

    index=num//10
    if num >= 10:
        columns = int(str(num)[1:])
    else:
        columns = num
    if array1[num] == 1:
        array1[num] = 0
        pygame.draw.circle(win,(255,0,0),((55+columns*width)+width//2,(55+index*width)+width//2),width//2,0)
        p2_counter += 1
        bombed_sound.play()
    elif array1[num] == 0:
        pygame.draw.circle(win,(0,0,0),((55+columns*width)+width//2,(55+index*width)+width//2),width//2,0)
    if p2_counter == 15:
        pygame.mixer.stop()
        text = font.render('You Lose...',1,(0,0,255))
        win.blit(text,(750-text.get_width()/2,200))
        pygame.display.update()
        lose.play()

    pygame.display.update()
    
def collback2(btn,i):
    def nothing2():
        btn.config(bg='#008000')
        bombing(i)
    return nothing2
  
def main():
    pygame.display.set_caption("battle ship")     
    win.fill((255,255,255)) 
    p1_field(win)
    p2_field(win)
    draw_ships(array_1,numbers)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        bomb_buttons()
        pygame.display.update()

    pygame.quit()

settingships()

  