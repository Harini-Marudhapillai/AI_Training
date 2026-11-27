
stack = []
top = -1

# Push
def push(x):
    global top
    stack.append(x)
    top += 1

# Pop
def pop():
    global top
    if top == -1:
        print("Stack is empty")
    else:
        print("Popped:", stack[top])
        stack.pop()
        top -= 1

# Peek
def peek():
    if top == -1:
        print("Stack is empty")
    else:
        print("Top element:", stack[top])


push(10)
push(20)
push(30)

peek()
pop()
peek()
