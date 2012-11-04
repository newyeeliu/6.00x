def laceStrings(s1, s2):
	result = ''
	len1 = len(s1)
	len2 = len(s2)

	for i in range(len1):
		result += s1[i]

		if i < len2:
			result += s2[i]

	i = len1

	while i < len2:
		result += s2[i]
		i += 1

	return result
