n = int(input())

arr = list(map(int, input().split()))
inc = [0 for i in range(n)]
dec = [0 for i in range(n)]

idx = max_length = 0

# 최댓값은 몇 번째 인덱스에 존재하나?
for i in range(n):
    if (arr[i] == max(arr)):
        idx = i

# 증가하는 수열 길이
for i in range(n):
    idx = i
    for j in range(i):
        if ((arr[j] < arr[i]) and (inc[idx] < inc[j])):
            idx = j
    inc[i] = inc[idx] + 1

# 감소하는 수열 길이
for i in range(n-1, -1, -1):
    idx = i
    for j in range(n-1, i-1, -1):
        if ((arr[j] < arr[i]) and (dec[idx] < dec[j])):
            idx = j
    dec[i] = dec[idx] + 1

for i in range(n):
    if (max_length < inc[i]+dec[i] - 1):
        max_length = inc[i]+dec[i] - 1

print(max_length)