import pygame
pygame.init()
screen = pygame.display.set_mode()
clock = pygame.time.Clock()
runing = True
dt = 0
#put varibeils here
map_image = "dev_map.png"
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
map = pygame.image.load(map_image).convert()
submap = map.subsurface(player_pos.x - 250,player_pos.y - 250 ,1player_pos.x + 250,player_pos.y + 250)
while runing:
  for evint in pygame.event.get():
     if pygame.event == pygame.QUIT:
        running = False
  #game updates here
      keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
        submap = map.subsurface(player_pos.x - 250,player_pos.y - 250 ,1player_pos.x + 250,player_pos.y + 250)
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
        submap = map.subsurface(player_pos.x - 250,player_pos.y - 250 ,1player_pos.x + 250,player_pos.y + 250)
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
        submap = map.subsurface(player_pos.x - 250,player_pos.y - 250 ,1player_pos.x + 250,player_pos.y + 250)
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
        submap = map.subsurface(player_pos.x - 250,player_pos.y - 250 ,1player_pos.x + 250,player_pos.y + 250)
  
  
  screen.fill("black")
  #render game here
  screen.blit(submap, (0, 0))
  pygame.draw.circle(screen , "red" , player_pos ,20)
  
  
  
  pygame.display.flip()
  clock.tick(60)
pygame.quit()
