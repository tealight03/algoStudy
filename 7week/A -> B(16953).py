n, m = map(int, input().split())
cnt = 1

while (n < m):
    if m % 10 == 1:
        m //= 10
    else:
        m /= 2
    cnt += 1

if n == m:
    print(cnt)
else:
    print(-1)