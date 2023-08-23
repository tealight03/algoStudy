import sys
input = sys.stdin.readline

s = list(input().rstrip())
t = list(input().rstrip())

flag = 0

while t:
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t.reverse()
    if s == t:
        flag = 1
        break

print(flag)