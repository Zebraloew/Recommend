class Node():
    #works
    def __init__(self, value):
        self.value = value
        self.next = None
    # works
    def setnext(self, next):
        self.next = next
    # not sure if this works
    def getnext(self):
        return self.next
    # not sure if this works
    def getvalue(self):
        return self.value
    # works
    def __str__(self):
        return "Node: " + str(self.value)
####

class LinkedList():
    # works
    def __init__(self, name):
        self.name = name
        self.length = 0
        self.head = None
    # works
    def sethead(self, node):
        self.head = node
    # works
    def __str__(self):
        return "LinkedList: " + str(self.name)
####


test = Node(1)
test2 = Node(2)
test.setnext(test2)
army = LinkedList("The Army")
army.sethead(test)

print(10*"\n")
print(str(test) + ", " + str(test2))
print(f"Value of test: {test.getvalue()}")
print(army)

print(str(test.next))
print(test.next.value)
print(f"Army Head: {army.head}")