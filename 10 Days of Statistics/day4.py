from random import random
import math as m

def permu(n,x):
    return m.factorial(n)/(m.factorial(x)*m.factorial(n-x))

def b(x,n,p):
    return permu(n,x)*(p**x)*((1-p)**(n-x))

##Challenge 1
# p = 1.09/2.09
# print(round(b(3,6,p)+b(4,6,p)+b(5,6,p)+b(6,6,p),3))

##Challenge 2
# print(round(b(2,10,0.12)+b(1,10,0.12)+b(0,10,0.12),3))
# print(round(1-(b(1,10,0.12)+b(0,10,0.12)),3))

##Challenge 3
# print(round(((2/3)**4)*(1/3),3))

##Challenge 4
# print(round(1-(2/3)**5,3))
