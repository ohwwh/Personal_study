def solution(customer):
	customer = sorted(customer, key=lambda x:x[0])
	start = customer[0][0]
	end = customer[0][1]
	answer = 0
	for e in customer:
		if e[0] >= start and e[1] <= end:
			continue
		if e[0] > end:
			answer += (end - start)
			start = e[0]
		if e[1] > end:
			end = e[1]
	answer += (end - start)
	return answer

customer = [[200,300],[100,200]]

print(solution(customer))