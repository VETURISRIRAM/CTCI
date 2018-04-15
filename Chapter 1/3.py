def duplicateRemoval(string):	
	for x in range(0, len(string)):
		for y in range(x+1, len(string)):
			if string[x] == string[y]:
				string = string.replace(string[y],"")
	return string

if __name__ == "__main__":
	s = "sriram"
	print(duplicateRemoval(s))
