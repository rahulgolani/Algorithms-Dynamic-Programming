# Recursive Solution
def breakSum(n):
    if n<=0:
        return 0
    return max(n,breakSum(n//2)+breakSum(n//3)+breakSum(n//4))

if __name__ == '__main__':
    n=12
    print(breakSum(n))


Dynamic Programming Solution
'''
def breakSum(n):
    dp=[0]*(n+1)
    dp[0]=0
    dp[1]=1
    for i in range(2,n+1):
        #print(dp[i//2],dp[i//3],dp[i//4],i)
        dp[i]=max(dp[i//2]+dp[i//3]+dp[i//4],i)
    print(dp)

    return dp[n]

n=3
print(breakSum(n))
'''
