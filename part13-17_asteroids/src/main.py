import pygame
from random import randint

pygame.init()
window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Asteroids")

robot = pygame.image.load("robot.png")
rock = pygame.image.load("rock.png")

robot_x = 320 - robot.get_width() / 2
robot_y = 480 - robot.get_height()
to_left = False
to_right = False

frames = 0
spawn_frames = 0
points = 0
play_checker = True

class Rock:
    def __init__(self):
        self.x = randint(0, 640 - rock.get_width())
        self.y = 0 - rock.get_height()

rocks = []

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
        if event.type == pygame.QUIT:
            exit()

    if play_checker:
        if frames == spawn_frames:
            rocks.append(Rock())
            frames = 0
            spawn_frames = randint(0, 300)

    if to_left and robot_x > 0:
        robot_x -= 3
    if to_right and robot_x < 640 - robot.get_width():
        robot_x += 3


    window.fill((0, 0, 0))
    game_font = pygame.font.SysFont("Arial", 24)
    text = game_font.render(f"Points: {points}", True, (255, 0, 0))
    window.blit(text, (535, 0))
    pygame.display.flip()
    window.blit(robot, (robot_x, robot_y))
    pygame.display.flip()
    for item in rocks:
        if item.y + rock.get_height() == 480:
            rocks = []
            play_checker = False
            break
        if item.y + rock.get_height() >= robot_y and ((item.x >= robot_x and item.x <= robot_x + robot.get_width()) or (item.x <= robot_x + robot.get_width() and item.x + rock.get_width() >= robot_x)):
            points += 1
            rocks.remove(item)
        
        window.blit(rock, (item.x, item.y))
        item.y += 1
        pygame.display.flip()
    
    
    if play_checker:
        frames += 1
    clock.tick(60)