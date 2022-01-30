# 큐
import sys
def push_func(num):
    queue.append(None)
    queue[len(queue)-1] = num

def pop_func():
    if len(queue) == 0:
        print(-1)
        return
    print(queue[0])
    del(queue[0])

def size_func():
    print(len(queue))

def empty_func():
    if len(queue) == 0:
        print(1)
    else:
        print(0)

def front_func():
    if len(queue)==0:
        print(-1)
        return
    print(queue[0])

def back_func():
    if len(queue)==0:
        print(-1)
        return
    print(queue[-1])

queue = []
n = int(sys.stdin.readline())
for _ in range(n):
    a = sys.stdin.readline().split()
    input = a[0]
    if input =="push":
        push_func(int(a[1]))
    elif input == "front":
        front_func()
    elif input == "back":
        back_func()
    elif input == "pop":
        pop_func()
    elif input == "size":
        size_func()
    elif input == "empty":
        empty_func()