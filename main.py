import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

map_image = "dock.png"
player_pos = pygame.Vector2(250, 250)
map_image_surface = pygame.image.load(map_image).convert()

def render(image, x, y):
    screen.blit(image, (x - player_pos.x, y - player_pos.y))

movement_speed = 300

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= movement_speed / 60
    if keys[pygame.K_s]:
        player_pos.y += movement_speed / 60
    if keys[pygame.K_a]:
        player_pos.x -= movement_speed / 60
    if keys[pygame.K_d]:
        player_pos.x += movement_speed / 60

    screen.fill((0, 0, 0))
    render(map_image_surface, 0, 0)
    w, h = pygame.display.get_surface().get_size()
    pygame.draw.circle(screen, (255, 0, 0), (w // 2, h // 2), 20)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

