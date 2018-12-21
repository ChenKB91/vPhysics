from visual import *
from vPhysics import *

def main():

	display1 = display(x=0, y=0, height=500, width=500, center = (0,0,0))
	Balls = PhysicScene(title='Balls', dt=0.001, display = display1)

	objs = []
	s2 = sqrt(2)/2
	GravObj(pos=vector(0.0, 0, 0), mass = 90000, v = vector(0,0,0),  do_gravity = True, scene = Balls, material = materials.wood)
	#GravObj(pos=vector(0, 100, 0), mass = 1, v =vector(3,-5,0), do_gravity = True, scene = Balls, make_trail=1, color = color.red)
	#sun = GravObj(pos=vector(-100, 0, 0), mass = 100, v =vector(10,0,0), do_gravity = True, scene = Balls, make_trail=1, color = color.orange)
	GravObj(pos=vector(100, 0, 0), mass = 10, v =vector(-s2*30,s2*30,0), do_gravity = False, scene = Balls,  make_trail=1, color = color.yellow)
	GravObj(pos=vector(-100, 0, 0), mass = 10, v =vector(s2*30,s2*30,0), do_gravity = False, scene = Balls,  make_trail=1, color = color.red)
	GravObj(pos=vector(100, 0, 0), mass = 10, v =vector(-s2*30,-s2*30,0), do_gravity = False, scene = Balls, make_trail=1, color = color.green)
	GravObj(pos=vector(-100, 0, 0), mass = 10, v =vector(s2*30,-s2*30,0), do_gravity = False, scene = Balls, make_trail=1, color = color.magenta)
	GravObj(pos=vector(100, 0, 0), mass = 10, v =vector(0,30,0), do_gravity = False, scene = Balls, make_trail=1, color = color.cyan)
	GravObj(pos=vector(-100, 0, 0), mass = 10, v =vector(0,-30,0), do_gravity = False, scene = Balls, make_trail=1, color = color.white)
	
	#objs.append(GravObj(pos=vector(225, 0, 0), mass = 1, v =vector(0,20,0), do_gravity = False, scene = Balls, make_trail=1))
	#indicator0 = arrow(pos = Balls.objects[0].pos, axis = Balls.objects[0].acc)


	while True:
		rate(5000)
		###########################################
		#indicator0.pos = Balls.objects[0].pos
		#indicator0.axis = Balls.objects[0].acc
		#print "i0 axis: ",indicator0.axis
		#print "i1 axis: ",indicator1.axis
		###########################################
		
		#print abs(Balls.objects[0].pos)
		#print abs(Balls.objects[1].pos)
		Balls.update()
		#Balls.display.center = sun.pos
		#print Balls.objects[0].pos-Balls.objects[1].pos


if __name__ == '__main__':
	main()