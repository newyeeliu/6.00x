def myLog(x, b):
	if x == 0:
		return 0
	log = 0

	while b**log <= x:
		log += 1

	return log - 1
