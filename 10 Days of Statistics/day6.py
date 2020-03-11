import math

def less_than(u,std,value):
	return 0.5*(1+math.erf((value-u)/(std*math.sqrt(2))))

def greater_than(u,std,value):
	return 1 - less_than(u,std,value)

def clt_less_than(u,std,n,limit):
	u2 = n*u
	std2 = math.sqrt(n)*std
	return less_than(u2,std2,limit)

def clt_greater_than(u,std,n,limit):
	u2 = n*u
	std2 = math.sqrt(n)*std
	return greater_than(u2,std2,limit)

##Challenge 1
#print(round(clt_less_than(205,15,49,9800),4))

##Challenge 2
#print(round(clt_less_than(2.4,2,100,250),4))

##Challenge 3
#n = 100
#u = 500
#std = 80
#z = 1.96
#a = u - (1/math.sqrt(n))*std*z
#b = u + (1/math.sqrt(n))*std*z
#print(round(a,2))
#print(round(b,2))


