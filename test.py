import pysics,time

pysics.init()
screen = pysics.screen()

key = pysics.key()
framerate = 60

objects = []
for i in range(0,1):
	objects.append(pysics.Object(texture = pysics.texture(), vertices = [pysics.vector(0,0),pysics.vector(0,100),pysics.vector(100,100),pysics.vector(100,0)],position=pysics.vector(0,0)))
	objects[i].texture.scale(100,100)

floor = pysics.Object(physics = True, color = (100,100,100), vertices = [pysics.vector(0,screen.height-100),pysics.vector(0,screen.height),pysics.vector(screen.width,screen.height),pysics.vector(screen.width,screen.height-100)], stroke = 0)


while 1:
	if round((time.time()) % (1/framerate),2)  == 0:
		screen.background.fill((255,255,255))
		floor.draw(screen)
		for poly in objects:
			if key.is_pressed('w'):
				poly.position.add(pysics.vector(0,1))
			if key.is_pressed('a'):
				poly.position.add(pysics.vector(-1,0))
			if key.is_pressed('s'):
				poly.position.add(pysics.vector(0,-1))
			if key.is_pressed('d'):
				poly.position.add(pysics.vector(1,0))		

		for poly in objects:
			poly.draw(screen)
		screen.update()






