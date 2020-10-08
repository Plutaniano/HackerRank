def absdiff(x,y):
	print(str(x) + "  " + str(y) )
	return abs(x-y)

def minimumAbsoluteDifference(arr):
	arr.sort()
	best = absdiff(arr[0],arr[1])
	for i in range(len(arr)-1):
		diff = absdiff(arr[i],arr[i+1])
		if diff < best:
			best = diff
	return best

