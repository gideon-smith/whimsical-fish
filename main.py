import pygame
import sys
pygame.init()
screen = pygame.display.set_mode()
clock = pygame.time.Clock()
running = True
dt = 0
#put varibeils here
map_image = "dock.png"
player_pos = pygame.Vector2(250, 250)
map = pygame.image.load(map_image).convert()
temporary_map = map 
submap = temporary_map.subsurface(player_pos.x - 250,player_pos.y - 250 ,player_pos.x + 250,player_pos.y + 250)
while running:
  for event in pygame.event.get():
     if pygame.event == pygame.QUIT:
        running = False
        sys.exit()
  #game updates here
  w, h = pygame.display.get_surface().get_size()   
  keys = pygame.key.get_pressed()
  if keys[pygame.K_w]:
      player_pos.y -= 300 * dt
      submap = temporary_map.subsurface(player_pos.x - 100,player_pos.y - 100 ,player_pos.x + 100,player_pos.y + 100)
      temporary_map = map
  if keys[pygame.K_s]:
      player_pos.y += 300 * dt
      submap = temporary_map.subsurface(player_pos.x - 100,player_pos.y - 100 ,player_pos.x + 250,player_pos.y + 100)
      temporary_map = map
  if keys[pygame.K_a]:
      player_pos.x -= 300 * dt
      submap = temporary_map.subsurface(player_pos.x - 100,player_pos.y - 100,player_pos.x + 100,player_pos.y + 100)
      temporary_map = map
  if keys[pygame.K_d]:
      player_pos.x += 300 * dt
      submap = temporary_map.subsurface(player_pos.x - 100,player_pos.y - 100 ,player_pos.x + 100,player_pos.y + 100)
      temporary_map = map
  
  screen.fill("black")
  #render game here
  screen.blit(map, (0, 0) )
  pygame.draw.circle(screen , "red" , (w/2 , h/2) ,20)
  
  
  
  pygame.display.flip()
  dt = clock.tick(60) / 1000
pygame.quit()
sys.exit()
