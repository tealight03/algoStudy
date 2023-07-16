n, k = map(int, input().split())

temp = list(map(int, input().split()))
total = ptr1 = 0
ptr2 = k

# 더미 값 넣기
for i in range(k):
    total += temp[i]

max_value = total

# --- 슬라이딩 윈도우로 구간 최대합 구하기 ---
while (ptr2 < n):
    total = total - temp[ptr1] + temp[ptr2]
    if max_value < total :
        max_value = total
    ptr1 += 1
    ptr2 += 1

print(max_value)