
import pygame
import sys
import math
import maps
pygame.init()
def arr_pos(x):
  return(math.trunc(x/1000000000000000000000000000000000000000000000000000000000000000000000000000000000))


screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
player_pos = pygame.Vector2(0,0)
main_map = pygame.image.load("asets/Sigma.png").convert()

def render(image, x, y):
    screen.blit(image, (x - player_pos.x, y - player_pos.y))
map_size = maps.Map_size
Map_image = main_map
map_image = Map_image
map = maps.Map
movement_speed = 0.5
dt = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and map[arr_pos(player_pos.x) + arr_pos(player_pos.y - movement_speed * dt) * map_size] == 0 :
        player_pos.y -= movement_speed * dt 
    if keys[pygame.K_s]  and map[arr_pos(player_pos.x) + arr_pos(player_pos.y + movement_speed * dt) * map_size] == 0:
        player_pos.y += movement_speed * dt 
    if keys[pygame.K_a] and map[arr_pos(player_pos.x - movement_speed * dt) + arr_pos(player_pos.y) * map_size] == 0:
        player_pos.x -= movement_speed  * dt
    if keys[pygame.K_d] and map[arr_pos(player_pos.x + movement_speed * dt) + arr_pos(player_pos.y) * map_size] == 0:
        player_pos.x += movement_speed * dt
    iii = 0
    screen.fill((0, 0, 0))
    w, h = pygame.display.get_surface().get_size()
    render(map_image,0,0)
    
        
    pygame.draw.circle(screen, (255, 0, 0), (w // 2, h // 2), 5)
    pygame.display.flip()
    dt = clock.tick(60)

pygame.quit()
sys.exit()

