MOD = 1000000007

def iegcd(a,b):
	x,y,u,v = 0,1,1,0
	while a != 0:
		q,r = b//a,b%a
		m,n =x-u*q,y-v*q
		b,a,x,y,u,v = a,r,u,v,m,n
	return b,x,y

def modinv(a):
	m = MOD
	g,x,y = iegcd(a,m)
	if g!= 1:
		return 1
	else:
		return x % m

def gj(m, eps=1.0/(10**10)):
	(h, w) = (len(m), len(m[0]))
	for y in range(0,h):
		maxrow = y
		for y2 in range(y+1,h):
			if abs(m[y2][y]) > abs(m[maxrow][y]):
				maxrow = y2
		(m[y], m[maxrow]) = (m[maxrow], m[y])
		if abs(m[y][y]) <= eps:
			return False
		for y2 in range(y+1,h):
			minv = modinv(m[y][y])
			c = m[y2][y]*minv
			for x in range(y,w):
				m[y2][x] -= m[y][x] * c
				m[y2][x] = m[y2][x] % MOD
	for y in range(h-1, 0-1,-1):
		c = m[y][y]
		modc = modinv(c)
		for y2 in range(0,y):
			for x in range(w-1,y-1,-1):
				m[y2][x] -= m[y][x]*m[y2][y]*modc
				m[y2][x] = m[y2][x] % MOD
		m[y][y] *= modc
		for x in range(h, w):
			m[y][x] *= modc
	return True


def solve(M, b):
	m2 = [row[:]+[right] for row, right in zip(M,b)]
	return [row[-1] for row in m2] if gj(m2) else None

def run():
	N = int(input())
	dp = list(map(int, input().split()))

	reached = set()
	reached.add(0)
	for _ in range(101):
		reached2 = set()
		for v in reached:
			for v2 in range(v + 1, min(N-1, v+7)):
				if dp[v2] == 0:
					reached2.add(v2)
				else:
					reached2.add(dp[v2]-1)
		reached = reached.union(reached2)
	rows = [[0]*(N) for _ in range(N)]
	b = [-1 % MOD]*(N)
	b[-1] = 0
	for i, v in enumerate(dp):
		rows[i][i] = -1 % MOD
		if not i in reached:
			continue
		for j in range(i+1, i+7):
			if j < N-1:
				if dp[j] == 0:
					rows[i][j] += modinv(6)
				else:
					rows[i][dp[j]-1] += modinv(6)
	for row in rows:
		for i in range(len(row)):
			row[i] = row[i] % MOD
	
	ans = solve(rows, b)
	print(ans[0] % MOD)

run()