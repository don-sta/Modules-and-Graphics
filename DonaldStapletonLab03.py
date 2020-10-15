# ETTG 1801
# Donald Stapleton
# Lab03 Modules
# Date: 09/20/2020

import time
import random
import pygame

pygame.display.init()

print("WELCOME TO THE RANDOM COLLAGE GENERATOR!")

w = int(input("Horizontal display resolution? "))
h = int(input("Vertical display resolution? "))

window = pygame.display.set_mode((w, h))

pygame.draw.circle(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                   (random.randint(0, w), random.randint(0, h)), 200, 0)
pygame.draw.polygon(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                    [(random.randint(0, w), random.randint(0, h)), (random.randint(0, w), random.randint(0, h)),
                     (random.randint(0, w), random.randint(0, h))], 0)
pygame.draw.rect(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                 (random.randint(0, w), random.randint(0, h), random.randint(20, w), random.randint(20, h)), 0)
pygame.draw.circle(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                   (random.randint(0, w), random.randint(0, h)), random.randint(20, 200), 0)
pygame.draw.polygon(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                    [(random.randint(0, w), random.randint(0, h)), (random.randint(0, w), random.randint(0, h)),
                     (random.randint(0, w), random.randint(0, h))], 0)
pygame.draw.rect(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                 (random.randint(0, w), random.randint(0, h), random.randint(20, w), random.randint(20, h)), 0)
pygame.draw.circle(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                   (random.randint(0, w), random.randint(0, h)), random.randint(20, 200), 0)
pygame.draw.polygon(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                    [(random.randint(0, w), random.randint(0, h)), (random.randint(0, w), random.randint(0, h)),
                     (random.randint(0, w), random.randint(0, h))], 0)
pygame.draw.rect(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                 (random.randint(0, w), random.randint(0, h), random.randint(20, w), random.randint(20, h)), 0)
pygame.draw.circle(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                   (random.randint(0, w), random.randint(0, h)), random.randint(20, 200), 0)
pygame.draw.polygon(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                    [(random.randint(0, w), random.randint(0, h)), (random.randint(0, w), random.randint(0, h)),
                     (random.randint(0, w), random.randint(0, h))], 0)
pygame.draw.rect(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                 (random.randint(0, w), random.randint(0, h), random.randint(20, w), random.randint(20, h)), 0)
pygame.draw.circle(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                   (random.randint(0, w), random.randint(0, h)), 200, 0)
pygame.draw.polygon(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                    [(random.randint(0, w), random.randint(0, h)), (random.randint(0, w), random.randint(0, h)),
                     (random.randint(0, w), random.randint(0, h))], 0)
pygame.draw.rect(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                 (random.randint(0, w), random.randint(0, h), random.randint(20, w), random.randint(20, h)), 0)
pygame.draw.circle(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                   (random.randint(0, w), random.randint(0, h)), random.randint(20, 200), 0)
pygame.draw.polygon(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                    [(random.randint(0, w), random.randint(0, h)), (random.randint(0, w), random.randint(0, h)),
                     (random.randint(0, w), random.randint(0, h))], 0)
pygame.draw.rect(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                 (random.randint(0, w), random.randint(0, h), random.randint(20, w), random.randint(20, h)), 0)
pygame.draw.circle(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                   (random.randint(0, w), random.randint(0, h)), random.randint(20, 200), 0)
pygame.draw.polygon(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                    [(random.randint(0, w), random.randint(0, h)), (random.randint(0, w), random.randint(0, h)),
                     (random.randint(0, w), random.randint(0, h))], 0)
pygame.draw.rect(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                 (random.randint(0, w), random.randint(0, h), random.randint(20, w), random.randint(20, h)), 0)
pygame.draw.circle(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                   (random.randint(0, w), random.randint(0, h)), random.randint(20, 200), 0)
pygame.draw.polygon(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                    [(random.randint(0, w), random.randint(0, h)), (random.randint(0, w), random.randint(0, h)),
                     (random.randint(0, w), random.randint(0, h))], 0)
pygame.draw.rect(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                 (random.randint(0, w), random.randint(0, h), random.randint(20, w), random.randint(20, h)), 0)
pygame.draw.circle(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                   (random.randint(0, w), random.randint(0, h)), 200, 0)
pygame.draw.polygon(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                    [(random.randint(0, w), random.randint(0, h)), (random.randint(0, w), random.randint(0, h)),
                     (random.randint(0, w), random.randint(0, h))], 0)
pygame.draw.rect(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                 (random.randint(0, w), random.randint(0, h), random.randint(20, w), random.randint(20, h)), 0)
pygame.draw.circle(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                   (random.randint(0, w), random.randint(0, h)), random.randint(20, 200), 0)
pygame.draw.polygon(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                    [(random.randint(0, w), random.randint(0, h)), (random.randint(0, w), random.randint(0, h)),
                     (random.randint(0, w), random.randint(0, h))], 0)
pygame.draw.rect(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                 (random.randint(0, w), random.randint(0, h), random.randint(20, w), random.randint(20, h)), 0)
pygame.draw.circle(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                   (random.randint(0, w), random.randint(0, h)), random.randint(20, 200), 0)
pygame.draw.polygon(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                    [(random.randint(0, w), random.randint(0, h)), (random.randint(0, w), random.randint(0, h)),
                     (random.randint(0, w), random.randint(0, h))], 0)
pygame.draw.rect(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                 (random.randint(0, w), random.randint(0, h), random.randint(20, w), random.randint(20, h)), 0)
pygame.draw.circle(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                   (random.randint(0, w), random.randint(0, h)), random.randint(20, 200), 0)
pygame.draw.polygon(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                    [(random.randint(0, w), random.randint(0, h)), (random.randint(0, w), random.randint(0, h)),
                     (random.randint(0, w), random.randint(0, h))], 0)
pygame.draw.rect(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                 (random.randint(0, w), random.randint(0, h), random.randint(20, w), random.randint(20, h)), 0)


pygame.display.update()

time.sleep(10)

pygame.quit()
