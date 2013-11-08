from raspirobotboard import *
import pygame
from pygame.locals import *

rr = RaspiRobot()

pygame.init()
screen = pygame.display.set_mode((640, 480))
font = pygame.font.SysFont("arial", 64)

pygame.display.set_caption('RaspiRobot')
pygame.mouse.set_visible(0)

def update_distance():
    dist = rr.get_range_inch()
    if dist > 0 and dist < 10:
        rr.stop()
        rr.set_led1(False)
        rr.set_led2(False)
    if dist == 0:
        return
    message = 'Distance: ' + str(dist) + ' in'
    text_surface = font.render(message, True, (127, 127, 127))
    screen.blit(text_surface, (100, 100))
    
    w = screen.get_width() - 20
    proximity = ((100 - dist) / 100.0) * w
    if proximity < 0:
        proximity = 0
    pygame.draw.rect(screen, (0, 255, 0), Rect((10, 10),(w, 50)))    
    pygame.draw.rect(screen, (255, 0, 0), Rect((10, 10),(proximity, 50)))
    pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP:
                rr.forward()
                rr.set_led1(True)
                rr.set_led2(True)
            elif event.key == K_DOWN:
                rr.set_led1(True)
                rr.set_led2(True)
                rr.reverse()
            elif event.key == K_RIGHT:
                rr.set_led1(False)
                rr.set_led2(True)
                rr.right()
            elif event.key == K_LEFT:
                rr.set_led1(True)
                rr.set_led2(False)
                rr.left()
            elif event.key == K_SPACE:
                rr.stop()
                rr.set_led1(False)
                rr.set_led2(False)
    screen.fill((255, 255, 255))
    update_distance()
