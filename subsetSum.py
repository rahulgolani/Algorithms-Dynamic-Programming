def subsetSum(S,m,n):
    dp=[[False for j in range(m+1)]for i in range(n+1)]
    for i in range(m+1):
        dp[0][i]=True #Base case
    for i in range(1,n+1):
        for j in range(1,m+1):
            if S[j-1]>i:
                dp[i][j]=dp[i][j-1]
            else:
                dp[i][j]=dp[i][j-1] or dp[i-S[j-1]][j-1]
    for i in range(len(dp)):
        print(dp[i])
    return dp[n][m]

if __name__ == '__main__':
    S=[3,4,5,2]
    print(subsetSum(S,len(S),6))
