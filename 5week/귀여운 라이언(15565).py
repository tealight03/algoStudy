leng, k = map(int, input().split())

doll = list(map(int, input().split()))
lion = []

for i in range(len(doll)):
    if doll[i] == 1:
        lion.append(i)

minleng = len(doll)
start = 0
end = k-1

if len(lion) < k:
    print(-1)
    exit(0)

while end != len(lion):
    cnt = lion[end] - lion[start] + 1
    minleng = min(minleng, cnt)
    start += 1
    end += 1

print(minleng)