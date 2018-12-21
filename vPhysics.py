from __future__ import division
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

		self.grav_objs = list(filter(lambda obj: obj.__class__ == GravObj, self.objects))

	def update_special_objs(self):
		self.grav_objs = list(filter(lambda obj: obj.__class__ == GravObj, self.objects))
		
	def update(self):
		field = ForceFieldFunction(self.grav_objs)
		for obj in self.grav_objs:
			if 1:
				obj.acc = vector(field(obj.pos))
				##print obj.acc
				obj.OnUpdate(self.dt)
			


class __BasePhysicObj(object):
	def __init__(self, scene, pos=vector(0), v=vector(0), color=(1,1,1), material=None):
		self.scene = scene
		self.acc = vector(0)
		self.pos, self.v = pos, v
		self.scene.objects.append(self)
		self.color = color
		self.material = material


		
class GravObj(__BasePhysicObj):
	"""docstring for GravObj"""

	def __init__(self,
				 mass,
				 do_gravity,  # to calculate the gravity caused by the obj
				 scene, make_trail=False, pos=vector(0), v=vector(0), radius = 'auto',
				 color=color.white, material = None):

		#__BasePhysicObj.__init__()
		super(GravObj, self).__init__(scene, pos, v, color, material)
		
		self.mass = mass
		self.do_gravity = do_gravity

		# add self into parent scene grav list
		self.scene.update_special_objs()
		#self.scene.grav_objs = list(filter(lambda obj: obj.__class__ == GravObj, self.scene.objects))

		if radius == 'auto':
			self.radius = self.mass**(1./3)
		else:
			self.radius = radius
		# appearance in vpython scene
		self.visual = sphere(radius=self.radius, pos = self.pos, make_trail = make_trail, retain = 1000,
		                     color = self.color, material = self.material) 


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


