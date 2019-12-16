import pygame
import os, sys
import time
import random
from random_texts import random_text
print(random_text)
pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = '100, 100'
W=1080
H=500
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("Python speed typing")
clock = pygame.time.Clock()

myfont_small = pygame.font.SysFont("monospace", 10)
myfont = pygame.font.SysFont("monospace", 15)
myfont_big = pygame.font.SysFont("monospace", 20)

input_text_rect = pygame.Rect(200, H//2, 700, 200)
input_text_lines = ["" for x in range(9)]
counter_il = 0
timer_started = False

pattern_text_rect = pygame.Rect(200, 50, 700, 180)
text_pattern_text = myfont_big.render("Pattern", 1, (188,188,255))
input_text_text = myfont_big.render("Your input", 1, (188,188,255))
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            print(input_text)
            exit()
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            if input_text_rect.collidepoint(mouse_pos) and timer_started == False:
              timer_started = True
              start_time = time.time()
        if timer_started == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input_text_lines[counter_il] = input_text_lines[counter_il][:-1]
                else:
                    input_text_lines[counter_il] += event.unicode

    if  (65 <= len(input_text_lines[counter_il]) <= 75 and input_text_lines[counter_il][-1] == " ") or (len(input_text_lines[counter_il])>75) :
        counter_il += 1
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,255,255), pattern_text_rect)
    if timer_started == True:
        timer_text = myfont.render("Time: %.2f" % (time.time()-start_time), 1, (0,255,0))
        pattern_text = random_text
        pattern_text_list = pattern_text.split()
        pattern_text_lines = ["" for x in range(9)]
        input_text = "".join(input_text_lines)
        cpm_text = myfont.render("CPM: %.2f" % (len(input_text)/((time.time()-start_time)/60)), 1, (0,255,0))     
        screen.blit(text_pattern_text, (pattern_text_rect.x*2.5, pattern_text_rect.y-22))
        c = 0
        for word in pattern_text_list:
            if len(pattern_text_lines[c]) < 60:
                pattern_text_lines[c] += word + " "
            else:
                pattern_text_lines[c] += word + " "
                c+=1
        c = 0
        pattern_bg = (255,255,255)
        for letter in range(len(input_text)):
            if input_text[letter] != pattern_text[letter]:
                pattern_bg = ((255,0,0))
        if input_text == pattern_text[:len(input_text)]:
            pattern_bg = ((0,255,0))
        pygame.draw.rect(screen, pattern_bg, pattern_text_rect)
        for line in pattern_text_lines:
            pattern_text_blit = myfont.render(line, 1, (0,0,0))
            screen.blit(pattern_text_blit, (pattern_text_rect.x +5, pattern_text_rect.y +5 + c))
            c+=20
        screen.blit(timer_text, (input_text_rect.x*2.2, H-30))
        screen.blit(cpm_text, (input_text_rect.x*2.8, H-30))
        if pattern_text == input_text:
            print("True")
            print("time: %.2f" % (time.time() - start_time))
            exit()

    pygame.draw.rect(screen, (255,255,255), input_text_rect)
    if timer_started == False:
        start_text = myfont_big.render("CLICK TO START", 1, (255,0,0))
        screen.blit(start_text, (input_text_rect.x*2.35, input_text_rect.y*1.3))
        pattern_text = myfont.render("Good luck!", 1, (0,0,0))
        screen.blit(pattern_text, (pattern_text_rect.x+5, pattern_text_rect.y+5))
    screen.blit(input_text_text, (input_text_rect.x*2.5, input_text_rect.y-22))


    for x in range(9):
        input_text_blit = myfont.render(input_text_lines[x], 1, (0,0,0))
        screen.blit(input_text_blit, (input_text_rect.x+5, input_text_rect.y+5+(x*20)))

    pygame.display.update()
    clock.tick(60)
