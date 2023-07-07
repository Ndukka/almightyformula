class code:
        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c
            
        def ans1(self):
            return ((-(self.b)) - ((self.b) ** 2 - (4 * (self.a) * (self.c))) ** (1/2)) * (1/(2 * a))
        #This is just (-b - (b^2 -4ac)**(1/2) * 1/(2*a))
        def ans2(self):
            return ((-(self.b)) + ((self.b) ** 2 - (4 * (self.a) * (self.c))) ** (1/2)) * (1/(2 * a))
            #This is just (-b + (b^2 -4ac)**(1/2) * 1/(2*a))
            
print("Nduka's Quadratic Equation Calculator")
while True:
    try:
        a = float(input("Enter the co-efficient of X^2:"))
        b = float(input("Enter the co-efficient of X:"))
        c = float(input("Enter the constant term:"))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
if a == 0:
    print("Error: This is not a valid quadratic equation")
else:
    print("The result of this quadratic equation is:", code(a, b, c).ans1(), "and", code(a, b, c).ans2())
    
