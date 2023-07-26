import sys
input = sys.stdin.readline

test = int(input())

for _ in range(test):
    n, m = map(int, input().split())

    for _ in range(m):
        a, b = map(int, input().split())
    print(n-1)