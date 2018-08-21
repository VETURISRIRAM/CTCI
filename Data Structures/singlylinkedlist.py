class Node:
	def __init__(self, dataval=None):
		self.dataval = dataval
		self.nextval = None

class SingleLinkedList:
	def __init__(self):
		self.headval = None

	def printlist(self):
		printval = self.headval
		while printval is not None:
			print(printval.dataval)
			printval = printval.nextval

	# def addnode(self, addition=None):
	# 	lastval = self.headval
	# 	if lastval.nextval is None:
	# 		lastval.nextval = self.addition



list1 = SingleLinkedList()

list1.headval = Node("Monday")
e2 = Node("Tuesday")
e3 = Node("Wednesday")
e4 = Node("Thursday")
e5 = Node("Friday")
e6 = Node("Saturday")

print(list1.headval.dataval)

list1.headval.nextval = e2
e2.nextval = e3
e3.nextval = e4
e4.nextval = e5
e5.nextval = e6

print(list1.headval.nextval.dataval)
print(e2.nextval.dataval)
print(e3.nextval.dataval)
print(e4.nextval.dataval)
print(e5.nextval.dataval)

print()
SingleLinkedList.printlist(list1)

# e7 = Node("DayAddition")
# SingleLinkedList.addnode(addition=e7)