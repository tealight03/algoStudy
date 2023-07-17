n, k = map(int, input().split())

arr = list(map(int, input().split()))

cnt = [0 for _ in range(100001)]
length = i = j = 0

while True:
    if i > j or j >= n:
        break

    if cnt[arr[j]] < k:
        cnt[arr[j]] += 1
        j += 1
        length = max(length, j - i)
    elif cnt[arr[j]] == k:
        cnt[arr[i]] -= 1
        i += 1

print(length)