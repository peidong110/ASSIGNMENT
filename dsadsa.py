	stringL = ''
	emptyList = []
	for i in range(size):
		empty = []
		for j in range(size):
			empty.append(0)
		emptyList.append(empty)
	for l in range(len(emptyList)):
		for k in range(len(emptyList[l])):
			stringL += str(emptyList[l][k])
			stringL += " "
	
		stringL += "\n"
	return stringL
