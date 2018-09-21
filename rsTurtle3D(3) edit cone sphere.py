import rhinoscriptsyntax as rs





class Turtle:
    def __init__(self, pos = [0,0,0], heading = [1,0,0]):
        self.heading = heading
        self.point = rs.AddPoint(pos)
        pointPos = rs.PointCoordinates(self.point)
        self.direction = rs.VectorCreate(heading,pointPos)
        self.lines = []
    
    def forward(self,magnitude):
        print self.direction
        movement = rs.VectorScale(self.direction,magnitude)
        prevPos = rs.PointCoordinates(self.point)
        rs.MoveObject(self.point,movement)
        currentPos = rs.PointCoordinates(self.point)
        rs.AddLine(prevPos,currentPos)
        
    def left(self,angle,(X,Y,Z)):

        self.direction = rs.VectorRotate(self.direction, angle, [X,Y,Z])
        print(self.direction)   
        
    def right(self,angle,(X,Y,Z)):
        self.direction = rs.VectorRotate(self.direction, -angle, [X,Y,Z])
        print(self.direction)
    
    def goto(self, x, y, z):
        prevPos = rs.PointCoordinates(self.point)
        movement = rs.VectorCreate([x,y,z],prevPos)
        rs.MoveObject(self.point,movement)
        currentPos = rs.PointCoordinates(self.point)
        
    def cube(self, l, w, h):
#        a = rs.AddPoint(self.point)
        p = rs.rs.PointCoordinates(self.point)
        a = rs.AddPoint(p)
        b = rs.CopyObject(a,[l,0,0])
        c = rs.CopyObject(a,[l,w,0])
        d = rs.CopyObject(a,[0,w,0])
        e = rs.CopyObject(a,[0,0,h])
        f = rs.CopyObject(a,[l,0,h])
        g = rs.CopyObject(a,[l,w,h])
        h = rs.CopyObject(a,[0,w,h])
        box = rs.AddBox([a,b,c,d,e,f,g,h])

    def cubecenter(self, m1, m2, m3):
#        a = rs.AddPoint(self.point)
        p = rs.GetPoint("Enter center point")
        a = rs.AddPoint(p)
        l = m1/2
        w = m2/2
        h = m3/2
        b = rs.CopyObject(a,[l,w,-h])
        c = rs.CopyObject(a,[l,-w,-h])
        d = rs.CopyObject(a,[-l,-w,-h])
        e = rs.CopyObject(a,[-l,w,-h])
        f = rs.CopyObject(a,[l,w,h])
        g = rs.CopyObject(a,[l,-w,h])
        h = rs.CopyObject(a,[-l,-w,h])
        j = rs.CopyObject(a,[-l,w,(m3/2)])
        box = rs.AddBox([b,c,d,e,f,g,h,j])

    def sphere(self, radius):
#        a = rs.AddPoint(self.point)
        p = rs.rs.PointCoordinates(self.point)
        a = rs.AddPoint(p)
        
        box = rs.AddSphere(a,radius)
      
    def cone(self, radius):
#        a = rs.AddPoint(self.point)
        base = rs.GetPoint("Base of cone")

        if base:

            height = rs.GetPoint("Height of cone", base)

        if height: rs.AddCone(base, height, radius, cap=False )
        
        
        
    def cylinder(self,r):
     a = rs.GetPoint("Enter start point")
     h = rs.GetReal("Enter the height")
     cylinder = rs.AddCylinder(a,h,r)
     
    def cylinders(self,num):
       a = rs.GetPoint("Enter start point")
       p = rs.AddPoint(a)
       h = rs.GetReal("Enter the height")
       for i in range(0,num):
           a.X = a.X + 4
           h = h + 5
           r = 2
           cylinder = rs.AddCylinder(a,h,r)
           color02 = [i * 3,i * 2,255 - i * 6] #magenta
           rs.ObjectColor(cylinder, color02)
           
           
    def jump(self,magnitude):
        a = rs.PointCoordinates(self.point)
        p = rs.AddPoint(a)
        sphere = rs.AddSphere(p,4)
        print self.direction
        prevPos = rs.PointCoordinates(self.point)
        for i in range(1,110):
         rs.MoveObject(sphere,(1,0,20 / i))
        for i in range(1,110):
         rs.MoveObject(sphere,(1,0,-1 * i / 40))
       
       
    def jumps(self,magnitude):
        a = rs.GetPoint("Enter start point")
        p = rs.AddPoint(a)
        sphere = rs.AddSphere(p,4)
        print self.direction
        prevPos = rs.PointCoordinates(self.point)
        for d in range(1,50):
         nn=rs.Redraw()
         for i in range(1,50):
          rs.MoveObject(sphere,(1,1,20 / i))
         for i in range(1,50):
          rs.MoveObject(sphere,(1,1,-1 * i / 40))


m=Turtle()






    
    
#m.sphere(5)
#m.cubecenter(10,10,10)
#m.cone(5)
#m.cylinder(5)
#m.cylinders(20)
#for i in range(10):
#    m.left(45,(0,-1,0))
#    m.forward(10)
    
#for i in range(10):
#    m.left(45,(-1,0,-1))
#    m.forward(10)
    
m.jumps(2)
