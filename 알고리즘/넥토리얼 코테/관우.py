import itertools

def getPower(e):
	ret = 0
	f = e[0]
	p = 0
	for i in e:
		if i == f:
			p += 1
		else:
			ret += ((ord(f)-96) ** p)
			p = 1
			f = i
	ret += ((ord(f)-96) ** p)
	return (ret)
		

def comb(arr, n):
	result = []
	if n == 0:
		return ([[]])
	for i in range(len(arr)):
		elem = arr[i]
		for rest in comb(arr[i + 1:], n - 1):
			target = [elem] + rest
			if target not in result:
				result.append([elem] + rest)
	return result

def getMaximumCombatPower(adventures, k):
	maxp = 0
	p = 0
	#com = set(itertools.combinations(adventures, k))
	com = comb(adventures, k)
	for e in com:
		p = getPower(e)
		if p > maxp:
			maxp = p
	return maxp

str = "abcc"
k = 2
print(getMaximumCombatPower(str, k))
#print(getPower(['a','b','c','c','c']))