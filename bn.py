import pygame
from pygame.locals import *
import random, math, sys

pygame.init()

Windows = pygame.display.set_mode((500, 400), 0, 32) # Main Surface
Antennas = [] #List of Antenna
FPS = 40
clock = pygame.time.Clock()
NBR_ANTENNA = 10
ANTENNA_RADIUS = 30

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SPEED = [10,10]
info = pygame.display.Info()
SW = info.current_w #Screen Width
SH = info.current_h #Screen Height

newcolour = lambda :(random.randint(100,250), random.randint(100,250), random.randint(100,250))
sub = lambda l1,l2:[l1[k]-l2[k] for k in range(len(l1))]





class Antenna:
	def __init__(self,radius=random.randint(20,100),x="auto",y="auto",sx="auto",sy="auto",color="auto"):
		self.radius = radius
		self.x = random.randint(self.radius, SW-self.radius) if x == "auto" else x
		self.y = random.randint(self.radius, SH-self.radius) if y == "auto" else y
		self.speedx = 0.5*(random.random()+1.0) if sx == "auto" else sx
		self.speedy = 0.5*(random.random()+1.0) if sy == "auto" else sy
		self.color = newcolour() if color == "auto" else color
	   	# self.mass = math.sqrt(self.radius)

A_LST = [Antenna(radius=ANTENNA_RADIUS,sx=5,sy=5) for k in range(NBR_ANTENNA)] #List of Antenna


def Collide(C1,C2):
	C1Speed = math.sqrt((C1.speedx**2)+(C1.speedy**2))
	XDiff = -(C1.x-C2.x)
	YDiff = -(C1.y-C2.y)
	if XDiff > 0:
		if YDiff > 0:
			Angle = math.degrees(math.atan(YDiff/XDiff))
			XSpeed = -C1Speed*math.cos(math.radians(Angle))
			YSpeed = -C1Speed*math.sin(math.radians(Angle))
		elif YDiff < 0:
			Angle = math.degrees(math.atan(YDiff/XDiff))
			XSpeed = -C1Speed*math.cos(math.radians(Angle))
			YSpeed = -C1Speed*math.sin(math.radians(Angle))
	elif XDiff < 0:
		if YDiff > 0:
			Angle = 180 + math.degrees(math.atan(YDiff/XDiff))
			XSpeed = -C1Speed*math.cos(math.radians(Angle))
			YSpeed = -C1Speed*math.sin(math.radians(Angle))
		elif YDiff < 0:
			Angle = -180 + math.degrees(math.atan(YDiff/XDiff))
			XSpeed = -C1Speed*math.cos(math.radians(Angle))
			YSpeed = -C1Speed*math.sin(math.radians(Angle))
	elif XDiff == 0:
		if YDiff > 0:
			Angle = -90
		else:
			Angle = 90
		XSpeed = C1Speed*math.cos(math.radians(Angle))
		YSpeed = C1Speed*math.sin(math.radians(Angle))
	elif YDiff == 0:
		if XDiff < 0:
			Angle = 0
		else:
			Angle = 180
		XSpeed = C1Speed*math.cos(math.radians(Angle))
		YSpeed = C1Speed*math.sin(math.radians(Angle))
	C1.speedx = XSpeed
	C1.speedy = YSpeed
def Move():
	for Antenna in A_LST:
		Antenna.x += Antenna.speedx
		Antenna.y += Antenna.speedy
def CollisionDetect():
	for Antenna in A_LST:
		if Antenna.x < Antenna.radius or Antenna.x > SW-Antenna.radius:    Antenna.speedx *= -1
		if Antenna.y < Antenna.radius or Antenna.y > SH-Antenna.radius:    Antenna.speedy *= -1
	for Antenna in A_LST:
		for A2 in A_LST:
			if Antenna != A2:
				if math.sqrt(  ((Antenna.x-A2.x)**2)  +  ((Antenna.y-A2.y)**2)  ) <= (Antenna.radius+A2.radius):
					Collide(Antenna,A2)
def Draw():
	Windows.fill(WHITE)
	for Antenna in A_LST:
		nc = tuple(sub(list(Antenna.color),[100,100,100]))
		pygame.draw.circle(Windows,Antenna.color,(int(Antenna.x),int(SH-Antenna.y)),Antenna.radius)
		pygame.draw.circle(Windows,nc,(int(Antenna.x),int(SH-Antenna.y)),Antenna.radius/4)
	pygame.display.flip()
def GetInput():
	keystate = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == QUIT or keystate[K_ESCAPE]:
			pygame.quit(); sys.exit()

def main():
	while True:
		GetInput()
		Move()
		CollisionDetect()
		Draw()
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
if __name__ == '__main__': main()