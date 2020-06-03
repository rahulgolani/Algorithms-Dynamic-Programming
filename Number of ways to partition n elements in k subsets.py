'''
def count(n,k):
    if n==0 or k==0 or k>n:
        return 0
    if k==1 or k==n:
        return 1
    return k*count(n-1,k)+count(n-1,k-1)

if __name__ == '__main__':
    n=3
    k=2
    print(count(n,k))
'''

# Time complexity O(2^n)

# Dynamic Programming Solution->

def count(n,k):
    dp=[[0 for j in range(k+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,k+1):
            # print(i,j)
            if i==j or j==1:
                dp[i][j]=1
            else:
                dp[i][j]=j*dp[i-1][j] + dp[i-1][j-1]
    for i in range(n+1):
        print (dp[i])

    return dp[n][k]

if __name__ == '__main__':
    n=3
    k=2
    print(count(n,k))
