n = int(input())
num = list(map(int, input().split()))
num.sort()

cnt = 0

# counting
for i in range(n):
    tmp = num[:i] + num[i+1:]
    start = 0
    end = len(tmp)-1

    while (start < end):
        mid = tmp[start] + tmp[end]

        if mid == num[i]:
            cnt += 1
            break
        elif mid > num[i]:
            end -= 1
        else:
            start += 1
        
print(cnt)