k, n  = map(int, input().split())

lan = []

for _ in range(k):
    lan.append(int(input()))

# 이분탐색으로 num 찾기 
num = max(lan)

mini = mid = 0
maxi = max(lan) + 1

while (mini < maxi):
    mid = (maxi + mini) // 2
    cnt = 0

    for i in lan:
        cnt += i // mid
    
    if cnt < n:
        maxi = mid
    else :
        mini = mid + 1

print(mini-1)