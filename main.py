import pygame #game originally made for https://repl.it/talk/share/How-much-can-you-do-in-115-lines-python/118007 but no longer conforms to that challenge due to pygame not being allowed in that challenge.
import random #random
pygame.init() #init pygame
sc = pygame.display.set_mode((500,240),pygame.FULLSCREEN)#screen
c = pygame.time.Clock()#clock for pacing program
#distance function
def dist(pos1,pos2):
	return ((pos2[0]-pos1[0])**2+(pos2[1]-pos1[1])**2)**0.5
#player
class Player:#player
	#init player
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.width = 16
	def draw(self): #draw player
		pygame.draw.circle(sc,(255,255,255),(self.x+(self.width/2),self.y-(self.width/2)),self.width)
	#update player
	def update(self):
		global snow
		self.y = 230-self.width
		#stop loop if too small
		if self.width < 2:
			snow = False
		#get pressed keys
		keys = pygame.key.get_pressed()
		#key d movement
		if keys[pygame.K_d]:
			self.x += 2
			self.width -= 0.05
		#key a movement
		if keys[pygame.K_a]:
			self.x -= 2
			self.width -= 0.05
		if self.x < -self.width: self.x = 500+self.width
		if self.x > 500+self.width: self.x = -self.width
#rock list
rocks = []
class Rock:
	#initiate rock
	def __init__(self):
		self.x = random.randint(1,500)
		self.y = -16
		self.width = 8
		self.color = (100,100,100)
		rocks.append(self)
	#draw rock
	def draw(self):
		pygame.draw.circle(sc,self.color,(self.x,self.y),self.width)
	#update rock
	def update(self):
		global snow
		self.y += 1
		if dist((self.x+4,self.y+4),(player.x+(player.width/2),player.y+(player.width/2))) < self.width+player.width:
			snow = False
		if self.y > 220-self.width: rocks.remove(self)
#snowball list
snowballs = []
class SnowBall:
	#initiate snowball
	def __init__(self):
		self.x = random.randint(1,500)
		self.y = -16
		self.width = 8
		self.color = (255,255,255)
		snowballs.append(self)
	#draw snowball
	def draw(self):
		pygame.draw.circle(sc,self.color,(self.x,self.y),self.width)
	#update snowball
	def update(self):
		global snow
		self.y += 1
		if dist((self.x+4,self.y+4),(player.x+(player.width/2),player.y+(player.width/2))) < self.width+player.width:
			player.width = 16
			snowballs.remove(self)
#define player and gameloop var
snow = True
player = Player(250,0)
#snow and rock timers
rock_timer = 120
snow_timer = 240
while snow:
	#decrease timers
	rock_timer -= 1
	snow_timer -= 1
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
	#spawn rocks
	if rock_timer <= 0:
		rock_timer = 120
		Rock()
	#spawn snowballs
	if snow_timer <= 0:
		snow_timer = 240*(player.width/16)
		SnowBall()
	#clear screen
	sc.fill((100,100,255))
	#draw and update rocks
	for i in rocks:
		i.update()
		i.draw()
	#draw and update snowballs
	for i in snowballs:
		i.update()
		i.draw()
	#update player
	player.update()
	#draw ground
	pygame.draw.rect(sc,(220,220,220),(0,220,500,20))
	#draw player
	player.draw()
	#update window
	pygame.display.flip()
	#pace program to 60fps
	c.tick(60)