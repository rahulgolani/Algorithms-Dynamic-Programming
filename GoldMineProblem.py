def goldMineProblem(goldMine,n,m):
    dp=[[0 for j in range(m)] for i in range(n)]
    #merge the conditions
    for j in range(m-1,-1,-1):
        for i in range(n):
            if j==m-1:
                right=0
                rightDown=0
                rightUp=0
            else:
                if i==0:
                    rightUp=0
                else:
                    rightUp=dp[i-1][j+1]

                right=dp[i][j+1]

                if i==n-1:
                    rightDown=0
                else:
                    rightDown=dp[i+1][j+1]
            # print(goldMine[i][j],rightUp,right,rightDown)
            dp[i][j]=goldMine[i][j]+max(right,rightUp,rightDown)
    result=dp[0][0]
    for i in range(1,n):
        # print(dp[i])
        if dp[i][0]>result:
            result=dp[i][0]
    return result

if __name__ == '__main__':
    goldMine=[[1,3,1,5],[2,2,4,1],[5,0,2,3],[0,6,1,2]]
    print(goldMineProblem(goldMine,4,4))
