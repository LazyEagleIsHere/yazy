import pygame
import random
import time
import sys
from pygame.math import Vector2
from text import *

pygame.init()

display_info = pygame.display.Info()
width, height = display_info.current_w, display_info.current_h
fps = 60
clock = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
gray = (200, 200, 200)
orange = (255, 165, 0)
yellow = (155, 155, 0)
light_blue = (173, 116, 233)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Yazy')
font = pygame.font.Font(None, 36)

def draw(text, font_size, y_position):
  font = pygame.font.Font(None, font_size)
  text_render = font.render(text, True, gray)
  text_rect = text_render.get_rect(center=(width // 2, y_position))
  screen.blit(text_render, text_rect)

def player_init():
  global player
  player = ""
  init = True
  
  while init:
    screen.fill(black)
    draw("YAZY!", 100, height // 4)
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          pygame.quit()
          sys.exit()
        elif event.key == pygame.K_RETURN:
          if player != "":
            init = False
        elif event.key == pygame.K_BACKSPACE:
          player = player[:-1]
        else:
          if '0' <= event.unicode <= '9':
            player += event.unicode
    
    player_surface = font.render(player, True, white)
    player_rect = player_surface.get_rect()
    player_rect.center = (width // 2, height // 2)
    screen.blit(player_surface, player_rect)
    
    text_surface = font.render("Number of players:", True, white)
    text_rect = text_surface.get_rect()
    text_rect.center = (width // 2, height // 2 - 80)
    screen.blit(text_surface, text_rect)
    
    pygame.display.update()
  
  start()

def start():
  screen.fill(black)
  
  base = [500, 100]
  basee = [base[0] + 10, base[1] + 10]
  round = 1
  die = [0 for _ in range(7)]
  lock = [0 for _ in range(7)]
  locka = [0 for _ in range(12)]
  roll = 0
  score = [[0 for _ in range(int(player))] for _ in range(12)]
  row_3 = 7
  row_4 = 8
  b25 = 9
  b40 = 10
  b50 = 11
  
  running = True
  while running:
    b1 = [Vector2(base[0], base[1]), 
          Vector2(width - base[0], base[1]), 
          Vector2(width - base[0], height - base[1]), 
          Vector2(base[0], height - base[1]), 
          Vector2(base[0], base[1])
        ]
    pygame.draw.polygon(screen, white, [(p.x, p.y) for p in b1])
    
    b2 = [Vector2(basee[0], basee[1]), 
          Vector2(width - basee[0] , basee[1]), 
          Vector2(width - basee[0], height - basee[1]), 
          Vector2(basee[0], height - basee[1]), 
          # Vector2(basee[0], basee[1])
        ]
    pygame.draw.polygon(screen, gray, [(p.x, p.y) for p in b2])
    
    mouse_pos = pygame.mouse.get_pos()
    
    roll_size = [600, 100]
    roll_button = pygame.Rect(width // 2 - 300, height - basee[1] * 2, roll_size[0], roll_size[1])
    
    if roll_button.collidepoint(mouse_pos) and roll != 3:
      write(screen, roll_button, "Roll", 65, "black", "gray69", 10)
    else:
      if roll == 3:
        write(screen, roll_button, "Roll", 65, "black", "red", 10)
      else:
        write(screen, roll_button, "Roll", 65, "black", "white", 10)
      
    b3 = [Vector2(width // 2 - 300, height - basee[1] * 2 - 100), 
          Vector2(width // 2 - 300 + roll_size[0], height - basee[1] * 2 - 100), 
          Vector2(width // 2 - 300 + roll_size[0], height - basee[1] * 2 - 100 + 90), 
          Vector2(width // 2 - 300, height - basee[1] * 2 - 100 + 90)
        ]
    pygame.draw.polygon(screen, orange, [(p.x, p.y) for p in b3])
    
    space = 37.5
    
    dice1 = pygame.Rect(width // 2 - 300, height - basee[1] * 2 - 100, 90, 90)
    if dice1.collidepoint(mouse_pos) and roll != 3 and not(lock[1]) and roll != 0:
      write(screen, dice1, str(die[1]), 65, "black", "gray69", 10)
    else:
      if lock[1] or roll == 3:
        write(screen, dice1, str(die[1]), 65, "black", "gray69", 10)
      else:
        write(screen, dice1, str(die[1]), 65, "black", "white", 10)
    
    dice2 = pygame.Rect(width // 2 - 300 + 90 + space, height - basee[1] * 2 - 100, 90, 90)
    if dice2.collidepoint(mouse_pos) and roll != 3 and not(lock[2]) and roll != 0:
      write(screen, dice2, str(die[2]), 65, "black", "gray69", 10)
    else:
      if lock[2] or roll == 3:
        write(screen, dice2, str(die[2]), 65, "black", "gray69", 10)
      else:
        write(screen, dice2, str(die[2]), 65, "black", "white", 10)
        
    dice3 = pygame.Rect(width // 2 - 300 + 90 * 2 + space * 2, height - basee[1] * 2 - 100, 90, 90)
    if dice3.collidepoint(mouse_pos) and roll != 3 and not(lock[3]) and roll != 0:
      write(screen, dice3, str(die[3]), 65, "black", "gray69", 10)
    else:
      if lock[3] or roll == 3:
        write(screen, dice3, str(die[3]), 65, "black", "gray69", 10)
      else:
        write(screen, dice3, str(die[3]), 65, "black", "white", 10)
    
    dice4 = pygame.Rect(width // 2 - 300 + 90 * 3 + space * 3, height - basee[1] * 2 - 100, 90, 90)
    if dice4.collidepoint(mouse_pos) and roll != 3 and not(lock[4]) and roll != 0:
      write(screen, dice4, str(die[4]), 65, "black", "gray69", 10)
    else:
      if lock[4] or roll == 3:
        write(screen, dice4, str(die[4]), 65, "black", "gray69", 10)
      else:
        write(screen, dice4, str(die[4]), 65, "black", "white", 10)
    
    dice5 = pygame.Rect(width // 2 - 300 + 90 * 4 + space * 4, height - basee[1] * 2 - 100, 90, 90)
    if dice5.collidepoint(mouse_pos) and roll != 3 and not(lock[5]) and roll != 0:
      write(screen, dice5, str(die[5]), 65, "black", "gray69", 10)
    else:
      if lock[5] or roll == 3:
        write(screen, dice5, str(die[5]), 65, "black", "gray69", 10)
      else:
        write(screen, dice5, str(die[5]), 65, "black", "white", 10)
    
    cnt_pos = [basee[0] + 10, basee[1] + 10]
    
    cnt_1_text = pygame.Rect(cnt_pos[0], cnt_pos[1], (width - cnt_pos[0]) // 2, 100)
    write(screen, cnt_1_text, "1", 65, "black", "yellow", 10)
    
    if not(locka[1]):
      score[round][1] = 0
    for i in range(1, 7):
      if die[i] == 1:
        score[round][1] += 1
    cnt_1 = pygame.Rect(width // 2, height // 2, 100, 100)
    if cnt_1.collidepoint(mouse_pos):
      write(screen, cnt_1, str(score[round][1]), 65, "black", "gray69", 10)
    else:
      write(screen, cnt_1, str(score[round][1]), 65, "black", "white", 10)
    
    # if not(locka[2]):
    #   score[round][2] = 0
    # for i in range(1, 7):
    #   if die[i] == 1:
    #     score[round][2] += 1
    # cnt_2 = pygame.Rect(width // 2, height // 2 + 150, 100, 100)
    # if cnt_2.collidepoint(mouse_pos):
    #   write(screen, cnt_2, str(score[round][2]), 65, "black", "gray69", 10)
    # else:
    #   write(screen, cnt_2, str(score[round][2]), 65, "black", "white", 10)
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          pygame.quit()
          sys.exit()
      elif event.type == pygame.MOUSEBUTTONDOWN:
        if roll_button.collidepoint(mouse_pos) and roll != 3:
          cnt = 0
          for i in range(1, 7):
            cnt += lock[i]
          if cnt != 6:
            roll += 1
            for i in range(1, 7):
              if not(lock[i]):
                die[i] = random.randint(1, 6)
        elif dice1.collidepoint(mouse_pos) and roll != 3 and roll != 0:
          if lock[1]:
            lock[1] = 0
          else:
            lock[1] = 1
        elif dice2.collidepoint(mouse_pos) and roll != 3 and roll != 0:
          if lock[2]:
            lock[2] = 0
          else:
            lock[2] = 1
        elif dice3.collidepoint(mouse_pos) and roll != 3 and roll != 0:
          if lock[3]:
            lock[3] = 0
          else:
            lock[3] = 1
        elif dice4.collidepoint(mouse_pos) and roll != 3 and roll != 0:
          if lock[4]:
            lock[4] = 0
          else:
            lock[4] = 1
        elif dice5.collidepoint(mouse_pos) and roll != 3 and roll != 0:
          if lock[5]:
            lock[5] = 0
          else:
            lock[5] = 1
        elif cnt_1.collidepoint(mouse_pos):
          locka[1] = 1
        
          
    
    pygame.display.flip()
    


running = True
while running:
  screen.fill(black)
  
  player_init()
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()

  pygame.display.flip()