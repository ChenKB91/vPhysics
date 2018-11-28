from visual import *

'''
.----------------.
| >>> vPhysics   |
| >>> By CKB     |
|______A___A_____| 
      (     )
     (    )  )
     [#######] 
This package is a application of VPython, an awesome python visualization package,
which is developed by David Scherer and others.

This package is designed to automatically do all the physics simulation.
You only need to declare the objects.

'''

#grav_const = 6.67E-11
grav_const = 1.


class PhysicScene():
	def __init__(self, title,  dt, display=None):

		self.title = title
		self.objects = []
		self.dt = dt
		self.display = display

		self.grav_objs = list(filter(lambda obj: obj.type == 'g', self.objects))

	def update(self):
		field = ForceFieldFunction(self.grav_objs)
		for obj in self.grav_objs:
			if 1:
				obj.acc = vector(field(obj.pos))
				##print obj.acc
				obj.OnUpdate(self.dt)
			


class __BasePhysicObj(object):
	def __init__(self, scene, pos=vector(0), v=vector(0)):
		self.scene = scene
		self.acc = vector(0)
		self.pos, self.v = pos, v
		self.scene.objects.append(self)


		
class GravObj(__BasePhysicObj):
	"""docstring for GravObj"""

	def __init__(self,
				 mass,
				 do_gravity,  # to calculate the gravity caused by the obj
				 scene, make_trail=False, pos=vector(0), v=vector(0)):

		#__BasePhysicObj.__init__()
		super(GravObj, self).__init__(scene, pos, v)
		self.type = 'g'
		self.mass = mass
		self.do_gravity = do_gravity

		# add self into parent scene grav list
		self.scene.grav_objs = list(filter(lambda obj: obj.type == 'g', self.scene.objects))

		# appearance in vpython scene
		self.visual = sphere(radius=self.mass**(1./3), pos = self.pos, make_trail = make_trail, retain = 10000) 


	def OnUpdate(self, dt):
		self.v += self.acc * dt
		self.pos += self.v * dt

		self.visual.pos = self.pos
		##print(self.acc)



def ForceFieldFunction(grav_objs):
	global grav_const
	grav_objs = [obj for obj in grav_objs if obj.do_gravity]
	#GM = array([grav_const * obj.mass for obj in grav_objs])

	def getAcc(p):
		acc_sum = vector(0)
		for obj in grav_objs:
			GM = grav_const * obj.mass
			R = obj.pos-p
			#print "R: ",R
			R3 = abs(R)**3
			#print "R3: ",R3
			if R3 > 0:
				acc = R*(GM/R3)
				#print "acc: ", acc
				#print "acc sum0: ", acc_sum
				acc_sum += acc
				#print "acc sum1: ", acc_sum
		
		#print "acc sum: ", acc_sum
		#print "---"
		return(acc_sum)

	return getAcc


def main():

	display1 = display(x=0, y=0, height=500, width=500, center = (0,0,0))
	Balls = PhysicScene(title='Balls', dt=0.01, display = display1)

	objs = []
	GravObj(pos=vector(0.0, 0, 0), mass = 90000, v = vector(0,0,0),  do_gravity = True, scene = Balls)
	GravObj(pos=vector(100, 0, 0), mass = 10, v =vector(0,10,0), do_gravity = False, scene = Balls, make_trail=1)
	GravObj(pos=vector(100, 0, 0), mass = 10, v =vector(0,20,0), do_gravity = False, scene = Balls, make_trail=1)
	GravObj(pos=vector(100, 0, 0), mass = 10, v =vector(0,30,0), do_gravity = False, scene = Balls, make_trail=1)
	GravObj(pos=vector(100, 0, 0), mass = 10, v =vector(0,30*sqrt(2),0), do_gravity = False, scene = Balls, make_trail=1)
	#objs.append(GravObj(pos=vector(225, 0, 0), mass = 1, v =vector(0,20,0), do_gravity = False, scene = Balls, make_trail=1))
	#indicator0 = arrow(pos = Balls.objects[0].pos, axis = Balls.objects[0].acc)


	while True:
		rate(1000)
		###########################################
		#indicator0.pos = Balls.objects[0].pos
		#indicator0.axis = Balls.objects[0].acc
		#print "i0 axis: ",indicator0.axis
		#print "i1 axis: ",indicator1.axis
		###########################################
		
		#print abs(Balls.objects[0].pos)
		#print abs(Balls.objects[1].pos)
		Balls.update()
		#print Balls.objects[0].pos-Balls.objects[1].pos


if __name__ == '__main__':
	main()
		
