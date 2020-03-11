import numpy as np
from sklearn import linear_model

m, n = list(map(int,input().split()))

f = []
y = []
for _ in range(n):
	f.append(list(map(float,input().split())))

for i in f:
	y.append(i.pop(-1))

lm = linear_model.LinearRegression()
lm.fit(f,y)
a = lm.intercept_
b = lm.coef_
b = b.tolist()
a = a.tolist()

for i in range(int(input())):
	var = []
	var = list(map(float,input().split()))
	total = 0
	for i in range(len(var)):
		total += b[i]*var[i]
	print(round(a+total,2))
