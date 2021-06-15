import pygame
pygame.init()
from time import sleep
pygame.font.init() 
myfont = pygame.font.SysFont('Comic Sans MS', 30)
screen = pygame.display.set_mode((500,500))
screen.fill((0,0,0))
pmx=70
pmy=250
pmr=30
obx=430
oby=70
obwidth=30
obheight=30
obstx=220
obsty=100
obstwidth=60
obstheight=400
pygame.draw.circle(screen,(255,255,0),(pmx,pmy),pmr)
pygame.draw.rect(screen, (255,0,0), (obx,oby, obwidth,obheight))
pygame.draw.rect(screen,(255,255,255),(obstx,obsty,obstwidth,obstheight))
pygame.display.flip()

def keys_handler():
  global pmx,pmy
  pygame.event.get()
  keys=pygame.key.get_pressed()
  if keys[pygame.K_UP]==1:
    pmy=pmy-5
  if keys[pygame.K_DOWN]==1:
    pmy=pmy+5
  if keys[pygame.K_LEFT]==1:
    pmx=pmx-5
  if keys[pygame.K_RIGHT]==1:
    pmx=pmx+5

def render():
  screen.fill((0,0,0))
  pygame.draw.circle(screen,(255,255,0),(pmx,pmy),pmr)
  pygame.draw.rect(screen, (255,0,0), (obx,oby, obwidth,obheight))
  pygame.draw.rect(screen,(255,255,255),(obstx,obsty,obstwidth,obstheight))
  pygame.display.flip()

def border():
  global pmx,pmy,pmr
  if pmx==500+pmr:
    pmx=0
  if pmx==-pmr:
    pmx=500+pmr
  if pmy==500+pmr:
    pmy=0
  if pmy==-pmr:
    pmy=500+pmr

while True:
  keys_handler()
  render()
  border()
  sleep(0.02)

if obstx-pmx < pmr or 