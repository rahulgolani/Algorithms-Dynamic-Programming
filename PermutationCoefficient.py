def permutationCoefficient(n,k):
    dp=[[0 for j in range(k+1)] for i in range(n+1)]
    for i in range(n+1):
        dp[i][0]=1
        for j in range(1,min(i,k)+1):
            dp[i][j]=dp[i-1][j]+j*dp[i-1][j-1]
    return dp[n][k]

if __name__ == '__main__':
    n=10
    k=2
    print(permutationCoefficient(n,k))
