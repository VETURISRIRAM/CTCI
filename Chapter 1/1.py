# Use ascii values
def isUnique1(string):
	if len(string) > 128:
		return False
	
	charSet = [False]*128
	for x in string:
		value = ord(x)
		if charSet[value] == True:
			return False
		charSet[value] = True
	return True


# Sort the list using sorted() which is nlogn 
def isUnique2(string):
	string = sorted(string)
	for x in range(1, len(string)):
		if string[x-1] == string[x]:
			return False
	return True
if __name__ == "__main__":
	s = "de"
	print(isUnique1(s))
	print(isUnique2(s))