import sys
import pygame
import asteroidfield
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps_clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    field = asteroidfield.AsteroidField()

    while True:
        dt = fps_clock.tick(60) / 1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))
        
        for obj in updatable:
            obj.update(dt)
            
            for asteroid in asteroids:
                for shot in shots:
                    if shot.collision(asteroid):
                        asteroid.split()
                        shot.kill()
                if player.collision(asteroid):
                    print("Game over!")
                    pygame.quit()
                    sys.exit()
            
        for obj in drawable:
            obj.draw(screen)
            
        pygame.display.flip()

if __name__ == "__main__":
    main()
