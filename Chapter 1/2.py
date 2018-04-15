def cReverse(string):
	return string[0:-1]

if __name__ == "__main__":
	s = "abcd\0"
	print(cReverse(s))