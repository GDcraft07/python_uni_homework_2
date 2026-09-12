import pygame
import random

def main():
    pygame.init()
    width, height = (600, 400)
    screen = pygame.display.set_mode((width, height))
    done = False

    target_radius = 15
    target_x, target_y = (0, 0)
    target_status = False
    target_hb = None

    bullet_radius = 8
    bullet_pos = pygame.Vector2(random.randint(bullet_radius, width - bullet_radius), height)
    bullet_vector = pygame.Vector2(target_x, target_y)
    bullet_status = False
    bullet_hb = None

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN and not bullet_status:
                if event.button == 1:
                    bullet_status = True
                    bullet_pos = pygame.Vector2(random.randint(bullet_radius, width - bullet_radius), height)
                    bullet_vector = (pygame.Vector2(target_x, target_y) - bullet_pos).normalize()

        if not target_status:
            target_status = True
            target_x, target_y = (random.randint(target_radius, width - target_radius), random.randint(target_radius, height - target_radius))
            target_hb = pygame.Rect(target_x - target_radius, target_y - target_radius, target_radius * 2, target_radius * 2)

        screen.fill((255, 255, 255))

        pygame.draw.circle(screen, (0, 0, 0), (target_x, target_y), target_radius)

        if bullet_status:
            pygame.draw.circle(screen, (0, 0, 0), bullet_pos, bullet_radius)

        pygame.display.flip()

if __name__ == "__main__":
    main()