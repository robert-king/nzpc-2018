def primes(upto):
	dp = [True] * (upto + 2)
	dp[0], dp[1] = False, False
	for i in range(2, upto+1):
		if dp[i]:
			yield i
			for j in range(i * i, upto + 1, i):
				dp[j] = False

print(len(list(primes(10**7))))