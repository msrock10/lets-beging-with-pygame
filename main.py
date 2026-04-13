import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

player = pygame.Rect(180, 180, 40, 40)
speed = 5

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    

    if keys[pygame.K_UP]:
        player.y -= speed
    

    if keys[pygame.K_DOWN]:
        player.y += speed

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), player)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()