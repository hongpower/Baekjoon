## 스택
import sys
def push_func(num):
    stack.append(None)
    stack[len(stack)-1] = num

def pop_func():
    if len(stack) == 0:
        print(-1)
        return
    print(stack[-1])
    del(stack[-1])

def size_func():
    print(len(stack))

def empty_func():
    if len(stack) == 0:
        print(1)
        return
    print(0)

def top_func():
    if len(stack) == 0:
        print(-1)
        return
    print(stack[-1])

stack = []
n = int(sys.stdin.readline())
for _ in range(n):
    a = sys.stdin.readline().split()
    input = a[0]
    if input =="push":
        push_func(int(a[1]))
    elif input == "top":
        top_func()
    elif input == "pop":
        pop_func()
    elif input == "size":
        size_func()
    elif input == "empty":
        empty_func()
