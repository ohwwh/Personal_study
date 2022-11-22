

def solution(a, b, budget):
	i = 0
	answer = 0
	while i*a <= budget:
		j = 0
		while j*b <= budget:
			if i*a + j*b == budget:
				answer += 1
			j += 1
		i += 1
	return answer


print(solution(3000, 5000, 23000))