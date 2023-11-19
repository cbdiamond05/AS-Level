# first.py
class First:
   pass
fr = First()
print (type(fr))
print (type(First))

# initialise.py
class Student:
   def __init__(self, name):
      self.name = name

student1 = Student('Kate')
student2 = Student('Katie')
student3 = Student('Cora')

print (student1.name)
print (student2.name)
print (student3.name)

# dynamic.py
class Dynamic:
   pass
d = Dynamic()
d.name = "Dynamic"
print (d.name)

# students.py
class Student:
   school = 'Assumption'

   def __init__(self, name, age, gender):
      self.name = name
      self.age = age
      self.gender = gender

Ronan = Student('Ronan', 16, 'Male')
Sarah = Student('Sarah', 17, 'Female')

print (Ronan.name, Ronan.age, Ronan.gender,Ronan.school)
print (Sarah.name, Sarah.age, Sarah.gender, Sarah.school)
print (Student.school)
print (Ronan.school)
print (Sarah.__class__.school)
print (student1.school)
print (student2.__class__.school)

# circle.py
class Circle:
   pi = 3.141592
   
   def __init__(self, radius=1):
      self.radius = radius 

   def area(self):
      return self.radius * self.radius * Circle.pi

   def setRadius(self, radius):
      self.radius = radius

   def getRadius(self):
      return self.radius

c = Circle()
c.setRadius(5)
print (c.getRadius())
print (c.area())

# methods.py
class Methods:
   def __init__(self):
      self.name = 'Methods'

   def getName(self):
      return self.name
m = Methods()
print (m.getName())
print (Methods.getName(m))

# inherit.py
class Animal:
   def __init__(self):
      print ("Animal created")

   def whoAmI(self):
      print ("Animal")

   def eat(self):
      print ("Eating")
      
class Dog(Animal):
   def __init__(self):
      Animal.__init__(self)
      print ("Dog created")

   def whoAmI(self):
      print ("Dog")

   def bark(self):
      print ("Woof!")
d = Dog()
d.whoAmI()
d.eat()

class Student:
    """The student class defines a student with attributes: name, age, form"""
    
    name="not set"
    age=1
    form="7"
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getForm(self):
        return self.form
    
    def setName(self, newName):
        self.name=newName
        
    def setAge(self, newAge):
        self.age=newAge
        
    def setForm(self, newForm):
        self.form=newForm
    
    def sayHello(self):
        print("Hello my name is ",self.name," I'm in form ",self.form)
        
student1=Student()
student1.setName("John")
print(student1.getName())
print(student1.sayHello())