
nums = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

while True:
	S = input().strip()
	if S == '#':
		break

	out = []
	buf = []
	S = list(S)
	S.append('')
	S.insert(0, '')
	for ch1, ch, ch2 in zip(S, S[1:], S[2:]):
		if ch in nums:
			buf.insert(0, ch)
		elif ch in ('-', '+', ',') and ch2 in nums:
			buf.insert(0, ch)
		elif ch == '.' and ch1 in nums and ch2 in nums:
			buf.insert(0, ch)
		else:
			for b in buf:
				out.insert(0, b)
			buf = []

			out.insert(0, ch)

	for b in buf:
		out.insert(0, b)

	print(''.join(out))