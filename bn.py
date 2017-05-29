import pygame, sys, time, random
from operator import sub
from pygame.locals import *

pygame.init()

windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Paint")

FPS = 40
clock = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SPEED = [10,10]
def newcolour():
	# any colour but black or white 
	return (random.randint(100,250), random.randint(100,250), random.randint(100,250))

sub = lambda l1,l2:[l1[k]-l2[k] for k in range(len(l1))]
NBR_ANTENNA = 10
ANTENNA_RADIUS = 40
info = pygame.display.Info()
sw = info.current_w
sh = info.current_h
def my_rand():
	pass
A_LST = [[random.randint(0,sw),random.randint(0,sh),ANTENNA_RADIUS,newcolour()] for k in range(NBR_ANTENNA)]

# print A_LST
windowSurface.fill(WHITE)
dx,dy = SPEED[0],SPEED[1]

k = 0 # Current Antenna In the list
n = 1 # Number of Hits
while True:
	#Draw all antenna
	windowSurface.fill(WHITE) #Clear Windows
	for a in A_LST:
		pygame.draw.circle(windowSurface, a[3] , (a[0],a[1]), a[2], 0)
		nc = tuple(sub(list(a[3]),[100,100,100]))
		print nc
		# print a[3]
		pygame.draw.circle(windowSurface, nc, (a[0],a[1]), ANTENNA_RADIUS/4, 0)
	if(k <= NBR_ANTENNA - 1):
		if A_LST[k][0] < 0 or A_LST[k][0] > sw:
			dx = -dx #Change course
			odx = dx
			n+=1
		else:
			pass
		if A_LST[k][1] < 0 or A_LST[k][1] > sh:
			dy = -dy #Change course
			ody = dy
			n+=1
		else:
			pass
		A_LST[k][0] += dx
		A_LST[k][1] += dy
		if n == 4:
			n = 0
			dx,dy=SPEED[0],SPEED[1]
			k+=1
			# dx,dy = 5,2
			# k+=1
	else:
		k=0
	pygame.display.update()
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()