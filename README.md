# SpringMass
Python Spring Mass Physics Engine


def Distance(self, mass1, mass2): #internal function for calculating distance between two Mass objects

def ConnectTo(self, mass2, k=1.0, MaxLengthFactor=2.0): #connect this mass to another one

def CollideWith(self, mass2, k=1.0): #turn on collision detection between this mass and another

def Move(self, dt=0.1,gravity=0.0): #translate the mass based on forces applied to it with Forces() and Collide()

def Forces(self): #calculate forces on the current mass based on its connections to other masses

def Collide(self): #calculate forces on the current mass based on its collision with other masses

Fixed = False #if true then the mass object does not move

x = 0.0 #x coordinate of mass in meters

y = 0.0 #y coordinate of mass in meters

vx = 0.0 #x velocity in m/s

vy = 0.0 #y velocity in m/s

mass = 10.0 #mass of the mass object in kilograms

diameter = 80.0 #diameter of mass object in meters

Create masses and connect them together. You can connect them with a collider object or a spring object.

When you have finished connecting all of your mass objects, you will need to create a main program loop

Inside the main loop, run Collide() and Forces() on each mass object. After that, use the Move(deltaTime, Gravity) function to translate the position of all the masses.

After that you can draw the masses on some sort of canvas.

Enjoy!
