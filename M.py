import sys
sys.setrecursionlimit(1000000000)

def dfs(i, j, e, rem):
	# print(i, j, e, rem)
	visited.add((i, j))

	if (i < L) and ((i + 1, j) not in visited) and (left[i] <= rem):
		if left[i] == rem:
			new_e = e + 1
			if new_e == E:
				return True

			new_rem = enemies[new_e]

		else:
			new_e = e
			new_rem = rem - left[i]

		if dfs(i + 1, j, new_e, new_rem):
			return True

	if (j < R) and ((i, j + 1) not in visited) and (right[j] <= rem):
		if right[j] == rem:
			new_e = e + 1
			if new_e == E:
				return True

			new_rem = enemies[new_e]

		else:
			new_e = e
			new_rem = rem - right[j]

		if dfs(i, j + 1, new_e, new_rem):
			return True

	return False


E, L, R = map(int, input().strip().split())

enemies = list(map(int, input().strip().split()))
left = list(map(int, input().strip().split()))
right = list(map(int, input().strip().split()))

if (sum(left) + sum(right)) < sum(enemies):
	print("NO")
else:
	visited = set()

	if dfs(0, 0, 0, enemies[0]):
		print("YES")
	else:
		print("NO")