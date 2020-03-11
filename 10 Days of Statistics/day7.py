import math

def mean(l):
	return sum(l)/len(l)

def std(ar):
    u = mean(ar)
    total = 0
    for i in ar:
        total += (i-u)**2
    return (total/len(ar))**0.5

def pearson_coef(dataset_x,dataset_y):
	u_x = mean(dataset_x)
	u_y = mean(dataset_y)
	n = len(dataset_x)
	soma = 0
	for x, y in zip(dataset_x,dataset_y):
		soma += (x-u_x)*(y-u_y)
	return soma/(n*std(dataset_x)*std(dataset_y))

def spearmans(dataset_x,dataset_y):
	n = len(dataset_x)
	x = dataset_x
	x_sorted = sorted(x)
	x_ranks = []
	y = dataset_y
	y_sorted = sorted(y)
	y_ranks = []
	for i, j in zip(x,y):
		x_ranks.append(x_sorted.index(i)+1)
		y_ranks.append(y_sorted.index(j)+1)
	d2_sum = 0
	for i, j in zip(x_ranks,y_ranks):
		d2_sum += (i-j)**2
	return 1-((6*d2_sum)/(n*(n**2-1)))


## Challenge 1
# print(round(pearson_coef(x,y),3))

## Challenge 2
#input()
#dataset_x = list(map(float,input().split()))
#dataset_y = list(map(float,input().split()))
#print(round(spearmans(dataset_x,dataset_y),3))

