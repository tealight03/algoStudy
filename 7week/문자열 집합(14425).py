import sys
input = sys.stdin.readline

n, m = map(int, input().split())
string = []
cnt = 0

for _ in range(n):
    string.append(input().rstrip())

for _ in range(m):
    str = input().rstrip()
    if str in string:
        cnt += 1

print(cnt)