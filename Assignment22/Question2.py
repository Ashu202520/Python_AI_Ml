class Circle:
    PI = 3.14

    def __init__(self, Radius = 0.0, Area = 0.0, Circumference = 0.0):
        self.Radius = Radius
        self.Area = Area
        self.Circumference = Circumference
    
    def Accept(self):
        self.Radius = float(input("Enter the radius of the circle:"))

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius
    
    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius
    
    def Display(self):
        print("Area of circle is:", self.Area)
        print("Circumference of circle is:", self.Circumference)
    
obj1 = Circle()

obj2 = Circle()

obj3 = Circle()

obj1.Accept()
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()

print("-" * 40)

obj2.Accept()
obj2.CalculateArea()
obj2.CalculateCircumference()
obj2.Display()

print("-" * 40)

obj3.Accept()
obj3.CalculateArea()
obj3.CalculateCircumference()
obj3.Display()
        