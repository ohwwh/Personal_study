N = 6

def getStatToDelete(stats):
	sm1 = sum(stats[2::2])
	sm2 = sum(stats[1::2])
	i = 0
	target = stats[i]
	for e in stats:
		if i % 2 == 0:
			if -sm1 + sm2 == 0:
				return i + 1
			else:
				if i < N - 1:
					sm2 += e
					sm2 -= stats[i + 1]
		else:
			if sm1 - sm2 == 0:
				return i + 1
			else:
				if i < N - 1:
					sm1 += e
					sm1 -= stats[i + 1]
		i += 1
	return -1

stats = [2, 5, 6, 7, 8, 4]
print(getStatToDelete(stats))