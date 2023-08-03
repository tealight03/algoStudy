n = int(input())
arr = list(map(int,input().split()))
result = [arr[0]]

for i in arr[1:]:
    start, end = 0,len(result)

    if i > result[-1]:
        result.append(i)
        continue
    
    while(start < end):
        mid = (start + end)//2
        
        if result[mid] < i:
            start = mid + 1
        else:
            end = mid

    if result[mid] >= i:
        result[mid] = i
    else:
        result[mid+1] = i
print(len(result))