import random
import pygame


CENTER = 300


class Person(pygame.sprite.Sprite):
    def __init__(self, status):

        def random_location():
            return random.randint(0, 400) - 200 + CENTER

        self.rect = pygame.Rect(0, 0, 5, 5)
        self.rect.center = (random_location(), random_location())
        self.status = status
        self.days_sick = 0
        self.dx = 0
        self.dy = 0

    def move(self):

        self.rect.x += self.dx
        self.rect.y += self.dy

        def random_speed():
            return random.randint(0, 20) / 10 - 1

        def gravity(x):
            gravity = (CENTER - x) ** 2 / 100000
            if x > CENTER:
                gravity *= -1
            return gravity

        self.dx += random_speed() + gravity(self.rect.x)
        self.dy += random_speed() + gravity(self.rect.y)
        DECELERATION = 0.99
        self.dx *= DECELERATION
        self.dy *= DECELERATION



    def color(self):
        if self.status == 'healthy':
            return (227,207,87)
        if self.status == 'healthy_conf':
            return (227,207,87)
        if self.status == 'sick':
            return (139,35,35)
        if self.status == 'sick_stop':
            return (139,35,35)
        if self.status == 'immune':
            return (67,205,128)
        if self.status == 'death':
            return (105,89,205)