import pygame
pygame.init()
from time import sleep
from random import randint
pygame.font.init() 
myfont = pygame.font.SysFont('Press Start 2P', 30)
screen = pygame.display.set_mode((500,500))
screen.fill((0,0,0))
pmxiniz=70
pmyiniz=250
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
obstheight=300
fail=False
success=False
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

def loss(pacman,obst):
  return ((obst[0]-pacman[2]<pacman[0]<obst[0]+obst[2]+pacman[2]) and (obst[1]<pacman[1]<obst[1]+obst[3]) or ((obst[0]<pacman[0]<obst[0]+obst[2]) and (obst[1]-pacman[2]<pacman[1]<obst[1]+obst[3]+pacman[2])))

def win(pacman,ob):
  return ((ob[0]-pacman[2]<pacman[0]<ob[0]+ob[2]+pacman[2]) and (ob[1]-pacman[2]<pacman[1]<ob[1]+ob[3]+pacman[2]))

def render():
  screen.fill((0,0,0))
  pygame.draw.circle(screen,(255,255,0),(pmx,pmy),pmr)
  pygame.draw.rect(screen, (255,0,0), (obx,oby, obwidth,obheight))
  pygame.draw.rect(screen,(255,255,255),(obstx,obsty,obstwidth,obstheight))
  if fail==True:
    screen.fill((0,0,0))
    textsurface=myfont.render("Hai perso",False,(255,255,255),None)
    screen.blit(textsurface,(100,240))
  if success==True:
    screen.fill((0,0,0))
    textsurface=myfont.render("Hai vinto",False,(255,255,255),None)
    screen.blit(textsurface,(100,240))
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

def next_state():
  global fail,success
  keys_handler()
  border()
  fail=loss((pmx,pmy,pmr),(obstx,obsty,obstwidth,obstheight))
  success=win((pmx,pmy,pmr),(obx,oby,obwidth,obheight))

while True:
  next_state()
  render()
  sleep(0.02)
  if fail==True:
    sleep(1.5)
    pmx=pmxiniz
    pmy=pmyiniz
  if success==True:
    sleep(1.5)
    pmx=pmxiniz
    pmy=pmyiniz
    obx=randint(0,500-obwidth)
    oby=randint(0,500-obheight)
    obstx=randint(pmx+pmr+1,500)
    obsty=randint(pmy+pmr+1,500)
    obstwidth=randint(10,500-2*pmr)
    obstheight=randint(10,500-2*pmr)