import pygame
pygame.init()
screen = pygame.display.set_mode(1280,720)
clock = pygame.time.Clock()
runing = true
#put varibeils here


while runing:
  for evint in pygame.event.get()
     if event.type == pygame.QUIT:
        running = False
  #game updates here
  
  
  
  screen.fill("black")
  #render game here
  
  
  
  
  pygame.display.flip()
  clock.tick(60)
pygame.quit()
