
ret = []



def postOrder(idx, message, l):
	if 2 * idx + 1 < l:
		postOrder(2 * idx + 1, message, l)
	if 2 * idx + 2 < l:
		postOrder(2 * idx + 2, message, l)
	ret.append(message[idx])


def solution(message):
	l = len(message)
	#message = list(message)
	postOrder(0, message, l)
	return "".join(s for s in ret)

message = "ABCDEF"

print(solution(message))