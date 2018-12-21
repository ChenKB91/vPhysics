from __future__ import division
from visual import*
#from visual.graph
from vPhysics import*
import math

def main():

	display1 = display(x=0, y=0, height=500, width=500, center = (0,0,0))
	Balls = PhysicScene(title='Lagrange', dt=0.001, display = display1)

	m1 = 1000000.
	m2 = 100.
	r1 = 200.
	v1 = math.sqrt((grav_const*m1)/r1)
	omega = v1/r1

	dr = r1*((m2/(m1+m2))**(1/3))
	rl1 = r1+dr
	rl2 = r1-dr
	#print rl1
	v2 = omega*rl1
	#v2 = math.sqrt((grav_const*m1)/rl1)

	sun = GravObj(pos=vector(0, 0, 0), mass = m1, v = vector(0,0,0),  do_gravity = True, scene = Balls, color = color.orange, radius = 100)
	planet = GravObj(pos=vector(r1, 0, 0), mass = m2, v = vector(0,v1,0),  do_gravity = True, scene = Balls, color = color.green, make_trail = True)
	L1 = GravObj(pos=vector(rl1, 0, 0), mass = 10, v = vector(0,v2,0),  do_gravity = False, scene = Balls, make_trail = True)
	#L2 = GravObj(pos=vector(rl2, 0, 0), mass = 10, v = vector(0,v2,0),  do_gravity = False, scene = Balls, make_trail = True)
	L3 = GravObj(pos=vector(r1/2, r1*(3**0.5)/2, 0), mass = 10,
				 v = vector(-v1*(3**0.5)/2,v1/2,0),  do_gravity = False, scene = Balls, make_trail = True)

	planet.visual.retain = 10000
	L3.visual.retain = 10000

	#L1.visual.retain = 10000

	while True:
		rate(500)
		Balls.update()


if __name__ == '__main__':
	main()