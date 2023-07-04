#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Code:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def ans1(self):
        return ((-(self.B)) - ((self.B) ** 2 - (4 * (self.A) * (self.C))) ** (1/2)) * (1/(2 * self.A))

    def ans2(self):
        return ((-(self.B)) + ((self.B) ** 2 - (4 * (self.A) * (self.C))) ** (1/2)) * (1/(2 * self.A))


while True:
    try:
        A = float(input("Enter the prefix of X^2: "))
        B = float(input("Enter the prefix of X: "))
        C = float(input("Enter the last number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if A == 0:
    print("Error: This is not a valid quadratic equation")
else:
    quadratic_eq = Code(A, B, C)
    print("The result of this quadratic equation is:", quadratic_eq.ans1(), "AND", quadratic_eq.ans2())

