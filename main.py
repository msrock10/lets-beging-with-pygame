import pygame
import random

pygame.init()

screen = pygame.display.set_mode((400, 400))

player = pygame.Rect(180, 350, 40, 40)
enemy = pygame.Rect(random.randint(0, 360), 0, 40, 40)

speed = 5
enemy_speed = 4

clock = pygame.time.Clock()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed

    enemy.y += enemy_speed

    if enemy.y > 400:
        enemy.y = 0
        enemy.x = random.randint(0, 360)

    if player.colliderect(enemy):
        print("Game Over")
        done = True

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (0, 255, 0), player)
    pygame.draw.rect(screen, (255, 0, 0), enemy)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()