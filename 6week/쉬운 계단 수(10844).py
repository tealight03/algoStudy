n = int(input())
cnt = 9 # n == 1일 때 

# n >= 2라면
if n >= 2:
    cnt = 3 + (n-1) * 14

print(cnt % 1000000000)