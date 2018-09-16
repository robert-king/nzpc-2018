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
			#print(m[y][y], minv)
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
	return [row[-1] for row in m2] if gj(m2) else 1

def run():
	N = int(input())
	dp = list(map(int, input().split()))
	if N <=2:
		print(1)
		return
	rows = [[0]*(N-1) for _ in range(N-1)]
	b = [-1 % MOD]*(N-1)
	for i, v in enumerate(dp[:-1]):

		rows[i][i] = -1 % MOD
		for j in range(i+1, i+7):
			if j < N-1:
				if dp[j] == 0:
					rows[i][j] += modinv(6)
					#print(i,j)
				else:
					rows[i][dp[j]-1] += modinv(6)
					#print(i,j,dp[j])
	for row in rows:
		#print('> ', row)
		for i in range(len(row)):
			row[i] = row[i] % MOD
	
	ans = solve(rows, b)
	#print(ans)
	print(ans[0] % MOD)

run()