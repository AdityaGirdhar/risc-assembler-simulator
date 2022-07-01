def binToDec(a, len):
	sum = 0
	for i in range(len):
		sum += int(a[i])*(2**(2-i))
	return sum
