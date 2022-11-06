S, P = map(int, input().split())

dna = str(input())
a, c, g, t = map(int, input().split())
start = 0
end = P - 1
ret = 0
for i in range(start, end + 1):
	if dna[i] == 'A':
		a -= 1
	elif dna[i] == 'C':
		c -= 1
	elif dna[i] == 'G':
		g -= 1
	elif dna[i] == 'T':
		t -= 1

if a <= 0 and c <= 0 and g <= 0 and t <= 0:
	ret += 1

while end < S - 1:
	if dna[start] == 'A':
		a += 1
	elif dna[start] == 'C':
		c += 1
	elif dna[start] == 'G':
		g += 1
	elif dna[start] == 'T':
		t += 1
	start += 1
	end += 1
	if dna[end] == 'A':
		a -= 1
	elif dna[end] == 'C':
		c -= 1
	elif dna[end] == 'G':
		g -= 1
	elif dna[end] == 'T':
		t -= 1
	if a <= 0 and c <= 0 and g <= 0 and t <= 0:
		ret += 1

print(ret)