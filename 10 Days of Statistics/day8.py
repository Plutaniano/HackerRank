def mean(l):
	return sum(l)/len(l)

def std(ar):
    u = mean(ar)
    total = 0
    for i in ar:
        total += (i-u)**2
    return (total/len(ar))**0.5

def angularCoef(x,y):
	sum_xy = 0
	sum_x2 = 0
	sum_x = sum(x)
	sum_y = sum(y)
	n = len(x)
	for i,j in zip(x,y):
		sum_xy += i*j
	for i in x:
		sum_x2 += i**2
	return ((n*sum_xy)-sum_x*sum_y)/(n*sum_x2-(sum_x**2))

def linearCoef(x,y):
	return mean(y)-angularCoef(x,y)*mean(x)

def SST(x):
	mean_x = mean(x)
	total = 0
	for i in x:
		total += (i-mean_x)**2
	return total

def SSR(x,y):
	a = linearCoef(x,y)
	b = angularCoef(x,y)
	mean_y = mean(y)
	new_y = []
	for xi in x:
		new_y.append(a+b*xi)
	total = 0
	for yi in new_y:
		total += (yi-mean(y))**2
	return total

def covariance(x,y):
	n = len(x)
	mean_x = mean(x)
	mean_y = mean(y)
	total = 0
	for i, j in zip(x,y):
		total += (i - mean_x)*(j - mean_y)
	return (1/n)*total



##Challenge 1
#x = [95, 85, 80, 70, 60]
#y = [85, 95, 70, 65, 70]
#print(round(linearCoef(x,y)+80*angularCoef(x,y),3))

##Challenge 2
#b1 = -3/4
#b2 = -3/4
#Pearsons = -3/4 or 3/4
#Both lines are downward sloping, so both x and y are negatively correlated
#Pearsons = -3/4