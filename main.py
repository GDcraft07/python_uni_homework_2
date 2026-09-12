import pygame
import random

def main():
    pygame.init()
    width, height = (600, 400)
    screen = pygame.display.set_mode((width, height))

    target_radius = 15
    target_x, target_y = (0, 0)
    target_status = False
    
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        if not target_status:
            target_x, target_y = (random.randint(target_radius, width - target_radius), random.randint(target_radius, height - target_radius))
            target_status = True

        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (0, 0, 0), (target_x, target_y), target_radius)

        pygame.display.flip()

if __name__ == "__main__":
    main()