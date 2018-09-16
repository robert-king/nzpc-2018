def get_int():
	return int(input())

names = []
d = {}
n = get_int()
for _ in range(n):
	names.append(input().strip())
	d[names[-1]] = 0

stuff = []
for _ in range(3*n):
	name, el, score = input().split()
	score = int(score)
	stuff.append((name, el, score))

rnd = input().strip()
mx = max(s for _, el, s in stuff if el == rnd)
for (name, el, score) in stuff:
	if el == rnd and score == mx:
		score += 5
	d[name] += score

winner = max(d, key=d.__getitem__)
loser = min(d, key=d.__getitem__)
print('%s gets immunity.' % winner)
print('%s goes home.' % loser)