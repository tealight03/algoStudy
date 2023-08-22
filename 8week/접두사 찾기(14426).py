import sys
input = sys.stdin.readline

n, m = map(int, input().split())
prefix = [input().strip() for _ in range(n)]
string = [input().strip() for _ in range(m)]
dic = {}
cnt = 0

for pre in prefix:
    for i in range(1,len(pre)+1): 
        dic[pre[:i]] = 1

for i in string:
    try:
        cnt += dic[i]
    except:
        pass
print(cnt)