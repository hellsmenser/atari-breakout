import pygame as pg
import math

#отскакивание мячика от поверхностей
def bounce(direction, diff):
	return ((180 - direction) % 360 - diff)

#класс блока
class Block():
	def __init__(self, x, y, color):
		self.image = pg.Surface([47, 20])
		self.image.fill(color)
		self.x = x
		self.y = y
		
#заполнение блоками
blocks = []
blockCount = 32

for row in range(5):
	for i in range(0, blockCount):
		print([205-(i*4), 0, 115+(i*2)])
		color = [205-(i*4)+(row * 3), 0, 115+(i*2)]
		curBlock = Block(i * (47 + 3), 100 + row * 21, color)
		blocks.append(curBlock)




#инициализация окна
size	= [800,600]
window	= pg.display.set_mode(size)
screen	= pg.Surface(size)
pg.display.set_caption('Arkanoid')

#инициализация платформы
platformPos		= [10,580]
platform		= pg.Surface([150,10])
moveFlagLeft	= False
moveFlagRight	= False
platform.fill([255,255,255])

#инициализация снаряда
balls		= 3
ball		= pg.Surface([20,20])
ballPos		= [300,400]
direction	= 200
ball.fill([255,0,0])
speed = 3.0

#запуск обновления окна
running = True
while running:
	for e in pg.event.get():
		if e.type  == pg.QUIT:
			running = False

		#управление
		elif e.type == pg.KEYDOWN:
			if e.key == ord('a'):
				moveFlagLeft = True
			if e.key == ord('d'):
				moveFlagRight = True
			#if e.key == ord('n') and death == True:
		elif e.type == pg.KEYUP:
			if e.key == ord('a'):
				moveFlagLeft = False
			if e.key == ord('d'):
				moveFlagRight = False
	#движение платформы
	if moveFlagRight and platformPos[0] < 650:
		platformPos[0] += 5
	if moveFlagLeft and platformPos[0] > 0: 
		platformPos[0] -= 5

	#движение шарика
	ballPos[0] -= speed * math.sin(math.radians(direction))	
	ballPos[1] += speed * math.cos(math.radians(direction))

	#отскок от стен
	if ballPos[0] <= 0:
		direction = (360 - direction) % 360
		ballPos[0] = 1
	if ballPos[0] >= 800:
		direction = (360 - direction) % 360
		ballPos[0] = 799
	if ballPos[1] <= 0:
		direction = bounce(direction, 0)
		ballPos[1] = 1
	if ballPos[1] > 600:
		death = True;

	#отскок от платформы
	if(ballPos[0] > platformPos[0] and ballPos[0] < platformPos[0]+150) and (ballPos[1]+3 >= platformPos[1]):
		diff = platformPos[0] + 75 - ballPos[0] - 10
		ballPos[1] = 600 - 10 - 20 - 1
		direction = bounce(direction, diff)


	#отрисовка
	screen.fill([0,0,0])
	screen.blit(ball, ballPos)
	screen.blit(platform, platformPos)
	for i in range(0, len(blocks)):
		curBlock = blocks[i]
		screen.blit(curBlock.image, [curBlock.x, curBlock.y])
	window.blit(screen, [0,0])
	pg.display.flip()
	pg.time.delay(5)

pg.quit()
