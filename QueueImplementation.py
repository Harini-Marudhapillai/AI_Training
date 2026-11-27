
queue = []
front = -1
rear = -1

# enqueue
def enqueue(x):
    global raer,front
    if front == -1:
        front+=1
        rear+=1
        queue[rear]=x
    else:
        rear+=1
        queue[rear]=x
    

# dequeue
def dequeue():
    global rear,front
    if front == -1:
        print("Queue is empty")
    else:
        front+=1

