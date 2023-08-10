import heapq

n = int(input())
card = []

for i in range(n):
    heapq.heappush(card,int(input()))

cnt = 0

if n == 1:
    print(0)
else:
    for i in range(n-1):
        tmp1 = heapq.heappop(card)
        tmp2 = tmp1 + heapq.heappop(card)
        cnt += tmp2
        heapq.heappush(card,tmp2)
        
    print(cnt)