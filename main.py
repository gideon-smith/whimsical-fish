import pygame
import sys
import math
pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
map_size = 3
player_pos = pygame.Vector2(0,0)
sand_tile = pygame.image.load("sand.png").convert()
lake_tile = pygame.image.load("lake_water.png").convert()
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

movement_speed = 300
dt = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= movement_speed * dt 
    if keys[pygame.K_s]:
        player_pos.y += movement_speed * dt
    if keys[pygame.K_a]:
        player_pos.x -= movement_speed  * dt
    if keys[pygame.K_d]:
        player_pos.x += movement_speed * dt
    iii = 0
    screen.fill((0, 0, 0))
    w, h = pygame.display.get_surface().get_size()
    for i in range(math.floor(len(map) / map_size)):
        for ii in range(map_size):
          iii  = iii + 1
          render(map[iii -1].file, ii * 25  , i * 25)
    
        
    pygame.draw.circle(screen, (255, 0, 0), (w // 2, h // 2), 20)
    pygame.display.flip()
    dt = clock.tick(60)

pygame.quit()
sys.exit()

