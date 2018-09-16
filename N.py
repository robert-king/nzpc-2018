N, M = map(int, input().strip().split())

T = []
for _ in range(N):
	T.append(int(input().strip()))

F = []
for _ in range(M):
	F.append(int(input().strip()))


test_is = [0, N-1]
max_t = max(T)


ts = 0
TCUM = [0]
for i, t in enumerate(T):
	ts += t
	TCUM.append(ts)

	if t == max_t:
		test_is.append(i)
		if i > 0:
			test_is.append(i-1)
		if i < (N-1):
			test_is.append(i+1)



tj = 0

for j in range(1, M):
	diff = max((TCUM[i+1] * F[j-1]) - (TCUM[i] * F[j]) for i in test_is)



	# print(_tj)
	# for i in range(N):
	# 	print (tj - (TCUM[i] * F[j]) + (TCUM[i+1] * F[j-1]))

	tj = max(tj, tj + diff)

# print(tj)
# print(TCUM)
# print(F)
# print(T)
print(tj + TCUM[-1] * F[-1])	
