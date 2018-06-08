import math

pi = math.pi


class Square:

    "This Class has the following parameters/attributes: side and units (optional and defaults to meters.) "    

    def __init__(self,side,units = "meters"):
        self.side = side
        self.units = units
    
    def __str__(self):
        return "The square has a side length of {} and the units are {}.".format(self.side,self.units)

    def area(self):
        return "The square has an area of {} {}.".format((self.side**2),self.units)
    
    def perimeter(self):
        return "The square has a perimeter of {} {}.".format((self.side*4),self.units)

class Rectangle:

    "This Class has the following parameters/attributes: width,length and Units (optional and defaults to meters.) "    

    def __init__(self,width,length,units = "meters"):
        self.width = width
        self.length = length
        self.units = units
    
    def __str__(self):
        return "The rectangle has a width of {} a length of {} and the units are in {}.".format(self.width,self.length,self.units)

    def area(self):
        return "The rectangle has an area of {} {}.".format(((self.width*2) + (self.length *2)),self.units)
    
    def perimeter(self):
        return "The rectangle has a perimeter of {} {}.".format((self.width*self.length),self.units)

class RightTriangle:

    "This shape has 3 parameters. Two of which are the legs of the triangle DO NOT SPECIFY THE HYPOTENEUSE, IT WILL BE CALCULATED AUTOMATICALLY. The last parameter is the units."
    
    def __init__(self,leg1,leg2,units = "meters"):
        self.leg1 = leg1
        self.leg2 = leg2
        self.units = units
        self.hypoteneuse = math.sqrt((self.leg1**2)+(self.leg2**2))

    def __str__(self):
        return "The right triangle has a leg of {} another of {} and a hypoteneuse of {}. The units are in {}.".format(self.leg1,self.leg2,self.hypoteneuse,self.units)

    def area(self):
        return "The area of the triangle is {} {}.".format(((self.leg1*self.leg2)/2),self.units)

    def perimeter(self):
        return "The perimeter of the triangle is {} {}.".format((self.leg1+self.leg2+self.hypoteneuse),self.units)


class Triangle:

    "This Class has the following parameters/attributes: side a(a), side b(b), and side c(c) and Units (optional and defaults to meters.) "    

    def __init__(self,a,b,c,units = 'meters' ):
        self.a = a
        self.b = b
        self.c = c
        self.units = units
        self.height = (self.a / self.b)*2
    
    def __str__(self):
        return "The triangle has the following measurements: a = {} b = {} c = {}. The units are {}.".format(self.a,self.b,self.c,self.units)
    
    def area(self):
        p = (self.a+self.b+self.c)/2
        def p_math(side):
            return p - side
        area = math.sqrt(p*p_math(self.a)*p_math(self.b)*p_math(self.c))
        return "The area of the triangle is {} {}.".format(area,self.units)

    def perimeter(self):
        return "The perimeter of the triangle is {} {}.".format((self.a+self.b+self.c),self.units)


class Circle:

    "This Class has the following parameters/attributes: radius and Units (optional and defaults to meters.) "    

    def __init__(self,radius,units = "meters"):
        self.radius = radius
        self.units  = units
    
    def __str__(self):
        return "The circle has a radius of {} and the units are in {}.".format(self.radius,self.units)

    def area(self):
        return "The area of the circle is {} {}.".format(pi*(self.radius**2),self.units)

    def circumference(self):
        return "The circumference of the circle is {} {}.".format((2*pi*self.radius),self.units)