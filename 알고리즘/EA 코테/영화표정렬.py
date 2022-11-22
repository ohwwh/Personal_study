def solution(movie):
	l = len(list(set(movie)))
	num = [0] * l
	dict = {}
	for e in movie:
		if e not in dict:
			dict[e] = 0
		else:
			dict[e] += 1
	dict = sorted(dict.items(), key=lambda x: (-x[1], x[0]))
	ret = []
	for e in dict:
		ret.append(e[0])
		
	return ret

movie = ["spy", "ray", "spy", "room", "once", "ray", "spy", "once"]
print(solution(movie))