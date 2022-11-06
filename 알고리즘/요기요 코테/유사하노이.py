def toString(lst):
    ret = ""
    for s in lst:
        ret += s
    return ret

def solution(stack1, stack2, stack3):
	ret = []
	while stack1 or stack2 or stack3:
		if not stack1:
			if not stack2:
				stack3.pop()
				ret.append(str(3))
			elif not stack3:
				stack2.pop()
				ret.append(str(2))
			else:
				if stack2[-1] >= stack3[-1]:
					stack2.pop()
					ret.append(str(2))
				else:
					stack3.pop()
					ret.append(str(3))
		elif not stack2:
			if not stack1:
				stack3.pop()
				ret.append(str(3))
			elif not stack3:
				stack1.pop()
				ret.append(str(1))
			else:
				if stack1[-1] >= stack3[-1]:
					stack1.pop()
					ret.append(str(1))
				else:
					stack3.pop()
					ret.append(str(3))
		elif not stack3:
			if not stack1:
				stack1.pop()
				ret.append(str(1))
			elif not stack2:
				stack2.pop()
				ret.append(str(2))
			else:
				if stack1[-1] >= stack2[-1]:
					stack1.pop()
					ret.append(str(1))
				else:
					stack2.pop()
					ret.append(str(2))
		else:	
			if stack1[-1] >= stack2[-1] :
				if stack1[-1] >= stack3[-1]:
					stack1.pop()
					ret.append(str(1))
				else:
					stack3.pop()
					ret.append(str(3))
			else:
				if stack2[-1] >= stack3[-1]:
					stack2.pop()
					ret.append(str(2))
				else:
					stack3.pop()
					ret.append(str(3))
	return toString(ret)


print(solution([2,7], [4,5], [1]))