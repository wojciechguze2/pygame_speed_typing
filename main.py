import pygame
import os, sys
import time
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

pattern_text = str(("x" * 15 +" ") * 25)
pattern_text_list = pattern_text.split()
pattern_text_lines = ["" for x in range(7)]
cc = 0
for _ in range(len(pattern_text_list)):
    if len(pattern_text_lines[cc])<=60:
        pattern_text_lines[cc] += (str(pattern_text_list[_]) +" ")
    else:
        cc += 1

pattern_text_rect = pygame.Rect(200, 50, 700, 150)
text_pattern_text = myfont_big.render("Pattern", 1, (188,188,255))
input_text_text = myfont_big.render("Your input", 1, (188,188,255))
#TODO: 
#      story generator
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        input_text = "".join(input_text_lines)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F5 and timer_started == False:
                timer_started = True
                start_time = time.time()
            elif event.key == pygame.K_ESCAPE:
                exit()
            elif event.key == pygame.K_END:
                print("False")
                print("time: %.2f" % (time.time()-start_time))
                exit()
            elif event.key == pygame.K_BACKSPACE:
                input_text_lines[counter_il] = input_text_lines[counter_il][:-1]
            else:
                input_text_lines[counter_il] += event.unicode
        if  len(input_text_lines[counter_il]) >=70 and input_text_lines[counter_il][-1] == " ":
            counter_il += 1
    if pattern_text == input_text:
        print("True")
        print("time: %.2f" % (time.time() - start_time))
        exit()

    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,255,255), pattern_text_rect)
    #pygame.draw.rect(
    screen.blit(text_pattern_text, (pattern_text_rect.x*2.5, pattern_text_rect.y-22))
    for a in range(len(pattern_text_lines)):
        pattern_line_blit = myfont.render(pattern_text_lines[a], 1, (0,0,0))
        screen.blit(pattern_line_blit, (pattern_text_rect.x+5, pattern_text_rect.y+5+(a*20)))
    
    pygame.draw.rect(screen, (255,255,255), input_text_rect)
    screen.blit(input_text_text, (input_text_rect.x*2.5, input_text_rect.y-22))

  
    for x in range(9):
        input_text_blit = myfont.render(input_text_lines[x], 1, (0,0,0))
        screen.blit(input_text_blit, (input_text_rect.x+5, input_text_rect.y+5+(x*20)))
    if timer_started == True:
        timer_text = myfont.render(("Timer: %.2f s" % (time.time() - start_time)), 1, (0,255,0))
        screen.blit(timer_text, (input_text_rect.x*2.5, input_text_rect.y+220))
    pygame.display.update()
    clock.tick(60)
