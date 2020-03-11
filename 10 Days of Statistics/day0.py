import math

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

def weightedMean(a,b):
    total = 0
    for i in range(len(a)):
        total += a[i]*b[i]
    return round(total/sum(b),1)

    
##Challenge 1
# a = input()
# a = input().split(" ")
# b = []
# for i in a:
#     b.append(int(i))
# print(mean(b))
# print(median(b))
# print(modal(b))

##Challenge 2
# a = input()
# a = input().split(" ")
# b = input().split(" ")
# x = []
# y = []
# for i in range(len(a)):
#     x.append(int(a[i]))
#     y.append(int(b[i]))

# print(weightedMean(x,y))
