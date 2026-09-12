import pygame
import random

def main():
    pygame.init()
    width, height = (600, 400)
    screen = pygame.display.set_mode((width, height))

    target_radius = 15
    target_x, target_y = (0, 0)
    
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        target_x, target_y = (random.randint(target_radius, width), random.randint(target_radius, height))
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (0, 0, 0), (target_x, target_y), target_radius)

        pygame.display.flip()

if __name__ == "__main__":
    main()