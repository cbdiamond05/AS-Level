# Create a class called “Fraction”, with the following attributes: numerator and denominator – these should initialise to (0/1), unless the user supplies another fraction. Create accessor functions called:	
# a.get_numerator() – return the numerator
# b.get_denominator() – return the denominator
# c.print_fraction() –prints the fraction
# d.print_type() – print the type of fraction (“proper” if the denominator is larger than the numerator, “improper” if the numerator is larger than the denominator)
# 
# And the following mutator function
# e.set_numerator() – takes a new numerator and set this as numerator
# f.set_denominator() – takes a new denominator and set this as denominator
# g.inverse() – change the numerator to the denominator and vice versa; this should not change if the numerator is 0
class Fraction:
    def __init__(self, numerator=0, denominator=1):
        self.numerator=numerator
        self.denominator=denomminator
        
    def get_numerator(self):
        return self.numerator
    
    def get_denominator(self):
        return self.denominator
    
    def print_fraction(self):
        self.fraction=fraction
        print(numerator,"/",denominator)
    
    def print_type(self):
        print(type(self.fraction))
        if numerator > denominator:
            print("Improper")
        else:
            print("Proper")
        
    def set_numerator(self, numerator):
      self.numerator=numerator
      
    def set_denominator(self, denominator):
      self.denominator=denominator
    
    def inverse(self):
        temp=self.numerator
        self.numerator=self.denominator
        self.denominator=temp

print(print_fraction)
print(print_type)


#Create a fraction with default values
fraction1 = Fraction()
print(fraction1.numerator, "/", fraction1.denominator)

# Create a fraction with user-supplied values
fraction2 = Fraction(3, 4)
print(fraction2.numerator, "/", fraction2.denominator)