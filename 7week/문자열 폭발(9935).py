import sys
input = sys.stdin.readline

string = input().rstrip()
bomb = list(input().rstrip())
stack = []

for s in string:
    stack.append(s)
    if len(stack) >= len(bomb):
        if stack[-len(bomb):] == bomb:
            for _ in range(len(bomb)):
                stack.pop()

if stack:
    for s in stack:
        print(s, end = "")
else:
    print("FRULA")