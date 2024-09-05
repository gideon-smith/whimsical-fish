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
def render(image , x , y):
    screen.blit(image, (x -player_pos.x,y - player_pos.y) )

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
  if keys[pygame.K_s]:
      player_pos.y += 300 * dt
  if keys[pygame.K_a]:
      player_pos.x -= 300 * dt
  if keys[pygame.K_d]:
      player_pos.x += 300 * dt

  
  screen.fill("black")
  #render game here
  render(map ,0,0)
  pygame.draw.circle(screen , "red" , (w/2 , h/2) ,20)
  
  
  
  pygame.display.flip()
  dt = clock.tick(60) / 1000
pygame.quit()
sys.exit()
