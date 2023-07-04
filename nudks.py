#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Nduka's Quadratic Equation Calculator")

while True:
    try:
        a = float(input("Enter the prefix of X^2:"))
        b = float(input("Enter the prefix of X:"))
        c = float(input("Enter the last number:"))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
if a == 0:
    print("Error: This is not a valid quadratic equation")
else:
    class Code:
        def __init__(self, A, B, C):
            self.A = A
            self.B = B
            self.C = C
        def Ans1(self):
            self.J = (1/(2 * a))
            
            return ((-(self.B)) - ((self.B) ** 2 - (4 * (self.A) * (self.C))) ** (1/2)) * (self.J)
            #Understand this might be a bit confusing, it is just the b**2 - 4ac, I know I can assign them to make it easier. 
        def Ans2(self):
            self.J = (1/(2 * a))
            
            return ((-(self.B)) + ((self.B) ** 2 - (4 * (self.A) * (self.C))) ** (1/2)) * (self.J)
        
    D = Code(a, b, c)
    print("The result of this quadratic equation is:", D.Ans1(), "AND", D.Ans2())


# In[ ]:




