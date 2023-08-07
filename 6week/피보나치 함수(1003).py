test = int(input())

for _ in range(test):
    num = int(input())
    dp = [[0,0] for i in range(num+1)]
    if num == 0:
        dp[0][0]= 1
        dp[0][1]= 0
    elif num == 1:
        dp[1][1] = 1
        dp[1][0] = 0
    elif num >= 2:    
        dp[0][0] = dp[1][1] = 1
        dp[0][1] = dp[1][0] = 0

        for i in range(2, num+1):
            dp[i][0] = dp[i-2][0] + dp[i-1][0]
            dp[i][1] = dp[i-2][1] + dp[i-1][1]

    print(f"{dp[num][0]} {dp[num][1]}")