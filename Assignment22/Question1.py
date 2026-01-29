class Demo:
    Value = 0
    def __init__(self, no1, no2):

        self.A = no1
        self.B = no2

    def fun(self):
        print(self.A, self.B)

    def gun(self):
        print(self.A, self.B)
    
obj1 = Demo(11,21)
obj2 = Demo(11,21)

obj1.fun()
obj2.fun()

obj1.gun()
obj2.gun()