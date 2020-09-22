# Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item or don’t pick it (0-1 property).

def knapsack(W,wt,val,n):

    dp=[[0 for j in range(W+1)] for i in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,W+1):
            if wt[i-1]<=j:
                dp[i][j]=max(dp[i-1][j],val[i-1]+dp[i-1][j-wt[i-1]])
            else:
                dp[i][j]=dp[i-1][j]
    # for i in range(len(dp)):
    #     print(dp[i])
    return dp[n][W]


W=50
wt=[10,20,30]
val=[60,100,120]
# W=7
# wt=[1,3,4,5]
# val=[1,4,5,7]
n=len(wt)
print(knapsack(W,wt,val,n))
