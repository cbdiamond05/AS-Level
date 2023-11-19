myStack = ["Alice", "Bob", "Sue", "Conor", "Mike", "Empty"]
pointerTop = 4

def pop():
    global pointerTop
    value = myStack[pointerTop]
    myStack[pointerTop] = "Empty"
    pointerTop -= 1
    return value

def push(data):
    global pointerTop
    pointerTop += 1
    myStack[pointerTop] = data

pop()
print(myStack)
push("Conor")
print(mystack)


myArray=[]

while pointerTop >= 0:
    myArray.append(pop())


print(myArray)
