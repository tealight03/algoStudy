import sys
input = sys.stdin.readline

s, p = map(int, input().split())
dna = list(input().rstrip())
count = [0, 0, 0, 0]
min_num = list(map(int, input().split()))
start = cnt = 0
end = p

def DNA_count(start, end):
    global cnt
    global count

    for i in range(start, end):
        if dna[i] == 'A':
            count[0] += 1
        elif dna[i] == 'C':
            count[1] += 1
        elif dna[i] == 'G':
            count[2] += 1
        else:
            count[3] += 1
            
    if (count[0] >= min_num[0]) and (count[1] >= min_num[1]) and (count[2] >= min_num[2]) and (count[3] >= min_num[3]):
        cnt += 1

DNA_count(start, end)

for i in range(end, s):
    if dna[i] == 'A':
        count[0] += 1
    elif dna[i] == 'C':
        count[1] += 1
    elif dna[i] == 'G':
        count[2] += 1
    elif dna[i] == 'T':
        count[3] += 1

    if dna[i-p] == 'A':
        count[0] -= 1
    elif dna[i-p] == 'C':
        count[1] -= 1
    elif dna[i-p] == 'G':
        count[2] -= 1
    elif dna[i-p] == 'T':
        count[3] -= 1

    if (count[0] >= min_num[0]) and (count[1] >= min_num[1]) and (count[2] >= min_num[2]) and (count[3] >= min_num[3]):
        cnt += 1

print(cnt)