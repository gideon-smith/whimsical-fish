#praise the nut gods
import pygame
import sys
import math
pygame.init()
def arr_pos(x):
  return(math.trunc(x/25))

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
map_size = 3
player_pos = pygame.Vector2(0,0)
sand_tile = pygame.image.load("asets/sand.png").convert()
lake_tile = pygame.image.load("asets/lake_water.png").convert()
class sand:
  type = 0
  file = sand_tile
  sub_type = 0
class lake_water:
  type = 1
  file = lake_tile
def render(image, x, y):
    screen.blit(image, (x - player_pos.x, y - player_pos.y))
map = [1,2,3,4,5,6]
map[0] = sand()
map[1] = sand()
map[2] = sand()
map[3] = lake_water()
map[4] = lake_water()
map[5] = lake_water()

movement_speed = 0.5
dt = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and map[player_pos.x][arr_pos(player_pos.y - movement_speed * dt)].type == 0 :
        player_pos.y -= movement_speed * dt 
    if keys[pygame.K_s]  and map[player_pos.x][arr_pos(player_pos.y + movement_speed * dt)].type == 0:
        player_pos.y += movement_speed * dt 
    if keys[pygame.K_a] and map[arr_pos(player_pos.x - movement_speed * dt)][player_pos.y].type == 0:
        player_pos.x -= movement_speed  * dt
    if keys[pygame.K_d] and map[arr_pos(player_pos.x + movement_speed * dt)][player_pos.y].type == 0:
        player_pos.x += movement_speed * dt
    iii = 0
    screen.fill((0, 0, 0))
    w, h = pygame.display.get_surface().get_size()
    for i in range(math.floor(len(map) / map_size)):
        for ii in range(map_size):
          iii  = iii + 1
          render(map[iii -1].file, ii * 25  , i * 25)
    
        
    pygame.draw.circle(screen, (255, 0, 0), (w // 2, h // 2), 5)
    pygame.display.flip()
    dt = clock.tick(60)

pygame.quit()
sys.exit()

