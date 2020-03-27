import math

#DEFINE MASS CLASS
class Mass:

    #INITIALIZE VARIABLES
    Fixed = False
    x = 0.0
    y = 0.0
    vx = 0.0
    vy = 0.0
    ax = 0.0
    ay = 0.0
    fx = 0.0
    fy = 0.0
    mass = 10.0
    diameter = 80.0

    #INITIALIZE SPRING AND COLLIDER COLLECTION
    Springs = []
    Colliders = []

    #COMPUTE DISTANCE BETWEEN TWO MASSES
    def Distance(self, mass1, mass2):
        return math.sqrt(math.pow(mass1.x - mass2.x, 2) + math.pow(mass1.y - mass2.y, 2))

    #CREARE SPRING CONNECTION BETWEEN SELF AND OTHER MASS
    def ConnectTo(self, mass2, k=1.0, MaxLengthFactor=2.0):
        newSpring = Spring()
        newSpring.k = k
        newSpring.node = mass2
        newSpring.length = self.Distance(self, mass2)
        newSpring.maxlength = MaxLengthFactor * newSpring.length
        self.Springs.append(newSpring)

    #CREATE COLLIDER BETWEEN SELF AND OTHER MASS
    def CollideWith(self, mass2, k=1.0):
        newCollider = Collider()
        newCollider.k = k
        newCollider.node = mass2
        newCollider.length = (self.diameter/2) + (mass2.diameter/2)
        self.Colliders.append(newCollider)

    #MOVE MASS ONE STEP
    def Move(self, dt=0.1,gravity=0.0):
        if self.Fixed == False:
            self.ax = self.fx / self.mass
            self.ay = (self.fy / self.mass) + gravity
            self.vx += (self.ax * dt)
            self.vy += (self.ay * dt)
            self.x += (self.vx * dt)
            self.y += (self.vy * dt)

        self.fx = 0.0
        self.fy = 0.0

    #COMPUTE FORCES BETWEEN SELF AND CONNECTED
    def Forces(self):
        for sp in self.Springs:
            if self.Distance(self, sp.node) >= sp.maxlength:
                sp.broken = True
            
            if sp.broken == False:
                self.fx += (((self.Distance(self, sp.node) - sp.length) * sp.k) / sp.length) * (sp.node.x - self.x)
                self.fy += (((self.Distance(self, sp.node) - sp.length) * sp.k) / sp.length) * (sp.node.y - self.y)
                sp.node.fx += (((self.Distance(self, sp.node) - sp.length) * sp.k) / sp.length) * (self.x - sp.node.x)
                sp.node.fy += (((self.Distance(self, sp.node) - sp.length) * sp.k) / sp.length) * (self.y - sp.node.y)

    #COMPUTE COLLISION BETWEEN SELF AND CONNECTED
    def Collide(self):

        for cl in self.Colliders:
            if (self.Distance(self, cl.node) <= ((self.diameter / 2) + (cl.node.diameter / 2))):
                self.fx += (((self.Distance(self, cl.node) - cl.length) * cl.k) / cl.length) * (cl.node.x - self.x)
                self.fy += (((self.Distance(self, cl.node) - cl.length) * cl.k) / cl.length) * (cl.node.y - self.y)
                cl.node.fx += (((self.Distance(self, cl.node) - cl.length) * cl.k) / cl.length) * (self.x - cl.node.x)
                cl.node.fy += (((self.Distance(self, cl.node) - cl.length) * cl.k) / cl.length) * (self.y - cl.node.y)
 
#DEFINE SPRING CLASS
class Spring:
    k = 1.0
    length = 1
    maxlength = 2.0
    broken = False
    node = Mass()

#DEFINE COLLIDER CLASS
class Collider:
    k = 1.0
    length = 1.0
    node = Mass()
