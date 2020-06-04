'''
def count(S,m,n,result):
    if n==0:
        print(result)
        return 1
    if n<0:
        return 0
    if m<=0 and n>0:
        return 0
    return count(S,m-1,n,result)+count(S,m,n-S[m-1],result+str(S[m-1]))

S=[3,5,10]
result=count(S,len(S),20,"")
print(result)
'''

#Dynamic Programming solution->

'''
def coinChange(S,m,n):
    table=[[0 for j in range(m)]for i in range(n+1)]
    for i in range(m):
        table[0][i]=1#base case for n=0

    for i in range(1,n+1):
        for j in range(m):
            x=table[i-S[j]][j] if i-S[j]>=0 else 0
            y=table[i][j-1] if j>=1 else 0
            table[i][j]=x+y

    #for i in range(n+1):
    #    print(table[i])

    return table[n][m-1]
S=[1,5,6]
print(coinChange(S,len(S),7))
'''


# O(n) space solution

def coinChange(S,m,n):
    dp=[0 for i in range(n+1)]
    dp[0]=1
    for i in range(m):
        for j in range(S[i],n+1):
            dp[j]+=dp[j-S[i]]
    return dp[n]

if __name__ == '__main__':
    S=[1,5,6]
    print(coinChange(S,len(S),7))
