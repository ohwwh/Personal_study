
def solution_month(money, minratio, maxratio, ranksize, threshold):
	rt = (money // 100) * 100
	if rt < threshold:
		final_ratio = 0
	else:
		x = (rt - threshold) // ranksize
		final_ratio = minratio + x
		if final_ratio > maxratio:
			final_ratio = maxratio
	return money - int(rt * final_ratio / 100)

def solution(money, minratio, maxratio, ranksize, threshold, months):
	for _ in range(months):
		money = solution_month(money, minratio, maxratio, ranksize, threshold)
	return money


print(solution(12345678, 10, 20, 250000, 10000000, 4))