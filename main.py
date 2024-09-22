
import pygame
import sys
import math
pygame.init()
def arr_pos(x):
  return(math.trunc(x/25))
class _map:
  def __init__(T_map_image) :#T__map,T_map_images):
    map_image = T_map_image
    #_map = T__map
    #map_images = T_map_images
    #map_image = T_map_image
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
player_pos = pygame.Vector2(0,0)
main_map = pygame.image.load("asets/map.png").convert()

class sand:
  type = 0
  sub_type = 0
class lake_water:
  type = 1
def render(image, x, y):
    screen.blit(image, (x - player_pos.x, y - player_pos.y))
Map = _map()
Map.__init__(main_map) #, [[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()],[sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand(),sand()]],[0,0])
movement_speed = 0.5
dt = 0
map = Map
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and map._map[arr_pos(player_pos.x)][arr_pos(player_pos.y - movement_speed * dt)].type == 0 :
        player_pos.y -= movement_speed * dt 
    if keys[pygame.K_s]  and map._map[arr_pos(player_pos.x)][arr_pos(player_pos.y + movement_speed * dt)].type == 0:
        player_pos.y += movement_speed * dt 
    if keys[pygame.K_a] and map._map[arr_pos(player_pos.x - movement_speed * dt)][arr_pos(player_pos.y)].type == 0:
        player_pos.x -= movement_speed  * dt
    if keys[pygame.K_d] and map._map[arr_pos(player_pos.x + movement_speed * dt)][arr_pos(player_pos.y)].type == 0:
        player_pos.x += movement_speed * dt
    iii = 0
    screen.fill((0, 0, 0))
    w, h = pygame.display.get_surface().get_size()
    render(map.map_image)
    
        
    pygame.draw.circle(screen, (255, 0, 0), (w // 2, h // 2), 5)
    pygame.display.flip()
    dt = clock.tick(60)

pygame.quit()
sys.exit()

