class Circle:
    pi = 3.141592
    
    def __init__(self, radius=1, name="Circle"):
        self.radius = radius
        self.name = name
    
    def calc_Diameter(self):
        return self.radius *2
    
    def calc_circumference(self):
        return 2 * Circle.pi * self.radius

    def calc_area(self):
      return Circle.pi * self.radius **2

    def set_radius(self, radius):
      self.radius = radius

    def set_name(self):
      self.name=name
    
    
circle1 = Circle()
circle1.set_name("First circle")
circle1.set_radius(3)

print (circle1.calc_Diameter())
print (circle1.calc_circumference())
print (circle1.calc_area())

    
circle2 = Circle()
circle2.set_name("Second Circle")
circle2.set_radius(5)

print (circle2.calc_Diameter())
print (circle2.calc_circumference())
print (circle2.calc_area())
    
    
    
    