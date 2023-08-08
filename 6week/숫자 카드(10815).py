def binary_search(key, card):
    start, end = 0, len(card)
    
    while(start < end):
        mid = (start + end) // 2

        if card[mid] == key:
            return 1
        elif card[mid] < key:
            start = mid+1
        else:
            end = mid
        
    return 0

n = int(input())
card = list(map(int, input().split()))
card.sort()

m = int(input())
comp = list(map(int, input().split()))

for data in comp:
    flag = binary_search(data, card)
    print(flag, end = " ")