import math

def weightedMean(a,b):
    total = 0
    for i in range(len(a)):
        total += a[i]*b[i]
    return round(total/len(a),1)

def removeDuplicates(ar):
    ar = list( dict.fromkeys(ar) )
    return ar

def mean(ar):
    return round(sum(ar)/len(ar),1)

def median(ar):
    ar.sort()
    if len(ar)%2 == 0:
        return (ar[int(len(ar)/2)-1] + ar[int(len(ar)/2)])/2
    else:
        return ar[(len(ar))/2]

def modal(ar):
    ar.sort()
    ar_noDuplicates = removeDuplicates(ar)
    best_key = 0
    best = 0
    for i in ar_noDuplicates:
        if ar.count(i) > best:
            best_key = i
            best = ar.count(i)
    return best_key

def std(ar):
    u = mean(ar)
    total = 0
    for i in ar:
        total += (i-u)**2
    return round((total/len(ar))**0.5,1)

def quartiles(ar):
    ar.sort()
    if len(ar) % 2 == 0:
        lower = ar[:int(len(ar)/2)]
        upper = ar[int(len(ar)/2):]
    else:
        lower = ar[:int(len(ar)/2)]
        upper = ar[int(len(ar)/2)+1:]
    return [lower,int(median(ar)),upper]

def interquartileRange(ar):
    q1, _, q3 = quartiles(ar)
    if len(q1) % 2 == 0:
        q1 = (q1[int(len(q1)/2)]+q1[int(len(q1)/2-1)])/2
    else:
        q1 = q1[int(len(q1)/2)]
    if len(q3) % 2 == 0:
        q3 = (q3[int(len(q3)/2)]+q3[int(len(q3)/2-1)])/2
    else:
        q3 = q3[int(len(q3)/2)]
    print(round(float(q3-q1),1))


##Challenge 1
# a = input()
# a = input().split(" ")
# b = []
# for i in a:
#     b.append(int(i))
# print(std(b))

##Challenge 2
#a = input()
#a = input().split(" ")
#b = []
#c = input().split(" ")
#d = []
#for i in range(len(a)):
#    b.append(int(a[i]))
#    d.append(int(c[i]))
#data = []
#for i in range(len(a)):
#    for _ in range(d[i]):
#        data.append(int(a[i]))
#interquartileRange(data)

##Challenge 3
# a = input()
# a = input().split(" ")
# b = []

# for i in a:
#     b.append(int(i))

# print(std(b))
