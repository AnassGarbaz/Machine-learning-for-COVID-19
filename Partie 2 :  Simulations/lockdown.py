import pygame
import random
import matplotlib.pyplot as plt
from person import Person

POPULATION = 1000
INITIAL_SICK = 5
CONF = 400
CONTAGIOUSNESS = 0.05
AVG_RECOVERY_TIME = 14

people = []
confine = []
for _ in range(INITIAL_SICK):
    people.append(Person(status='sick'))
for _ in range(POPULATION - CONF - INITIAL_SICK ):
    people.append(Person(status='healthy'))
for _ in range(CONF):
     people.append(Person(status='healthy_conf'))

clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption(' lockdown simulation')
screen = pygame.display.set_mode((600, 500), 0, 32)

running = True
graphed = False
data = [[], [], [], []]

while running:

    screen.fill((255, 255, 255))

    for ray in data:
        ray.append(0)

    for person in people:
        if person.status == 'healthy' or person.status == 'sick' or person.status == 'immune':
             person.move()
        if person.status == 'sick':
            data[0][len(data[0]) - 1] += 1

            for other_person in people:
                if other_person.status == 'healthy' and person.rect.colliderect(other_person.rect):
                    CONTRACT_PROB = random.randint(0, 100) / 100
                    if CONTAGIOUSNESS > CONTRACT_PROB:
                        other_person.status = 'sick'
                        CONTRACT_PROB = random.randint(0, 100) / 100
                        if CONTAGIOUSNESS > CONTRACT_PROB:
                            other_person.status = 'death'
                if other_person.status == 'healthy_conf' and person.rect.colliderect(other_person.rect):
                    CONTRACT_PROB = random.randint(0, 100) / 100
                    if CONTAGIOUSNESS > CONTRACT_PROB:
                        other_person.status = 'sick'
            person.days_sick += 2
            RECOVERY_PROB = (person.days_sick + random.randint(0, 10) - 5) / 10
            if AVG_RECOVERY_TIME < RECOVERY_PROB:
                person.status = 'immune'
        if person.status == 'immune':
            data[1][len(data[0]) - 1] += 1

        if person.status == 'healthy' or person.status == 'healthy_conf':
            data[2][len(data[0]) - 1] += 1
        if person.status == 'death':
            data[3][len(data[0]) - 1] += 1
        pygame.draw.rect(screen, person.color(), person.rect)

    if data[0][len(data[0]) - 1] == 0 and not graphed:
        plt.title('Contagion Spread Graph')
        x = range(len(data[0]))
        labels = ['immune','sick', 'healthy', 'death', 10]
        colors = ['green', 'red', 'yellow', 'blue', 'r']
        plt.stackplot(x, data, labels=labels, colors=colors)
        plt.legend(loc='upper left')
        plt.show()

        graphed = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(50)
