def getWaysToReachStairs(n):
    if n==0:
        return 1
    result1,result2,result3=0,0,0
    if (n-1)>=0:
        result1=getWaysToReachStairs(n-1)
    if (n-3)>=0:
        result2=getWaysToReachStairs(n-3)
    if (n-4)>=0:
        result3=getWaysToReachStairs(n-4)
    return result1+result2+result3

# if __name__ == '__main__':
#     n=4
#     print(getWaysToReachStairs(n))
#1=1,2=1,3=2,4=4

# dp solution

def getWaysToSumN(n):
    dp=[0]*(n+1)
    dp[0]=1
    dp[1]=1
    dp[2]=1
    dp[3]=2
    for i in range(4,n+1):
        dp[i]=dp[i-1]+dp[i-3]+dp[i-4]
    return dp[n]

if __name__ == '__main__':
    n=5
    result=getWaysToSumN(n)
    print(result)
