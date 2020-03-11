import math

def less_than(u,std,value):
	return 0.5*(1+math.erf((value-u)/(std*math.sqrt(2))))

def between(u,std,smaller,greater):
	return less_than(u,std,greater) - less_than(u,std,smaller)

def greater_than(u,std,value):
	return 1 - less_than(u,std,value)

##Problem 1
#print(round(less_than(20,2,19.5),3))
#print(round(between(20,2,20,22),3))

##Problem 2
#print(round(100*greater_than(70,10,80),2))
#print(round(100*greater_than(70,10,60),2))
#print(round(100*less_than(70,10,60),2))