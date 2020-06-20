'''
import sys
def cutRod(price,n):
    if n<=0:
        return 0
    max_val=-1

    for i in range(n):
        max_val=max(max_val,price[i]+cutRod(price,n-(i+1)))
    return max_val

arr=[1, 5, 8, 9, 10, 17, 17, 20]
# arr=[3,5,8,9]
n=len(arr)
result=cutRod(arr,n)
print(result)
'''
#Dynamic Programming soultion
'''
def cutRod(price,n):
    val=[[0 for j in range(n+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            # if j>=i:
            if j<=i:
                # val[i][j]=max(val[i-1][j],price[i-1]+val[i][j-i])
                val[i][j]=max(val[i][j-1],price[j-1]+val[i-j][j]) # max of either not cutting and cutting
            else:
                val[i][j]=val[i][j-1]
    # for i in val:
    #     print(i)
    return val[n][n]
arr=[1, 5, 8, 9, 10, 17, 17, 20]
# arr=[3,5,8,9]
n=len(arr)
result=cutRod(arr,n)
print(result)
'''


#using space of (n) and filling the table in bottom up order
def cutRod(price,n):
    val=[0 for i in range(n+1)]
    val[0]=0
    for i in range(1,n+1):
        max_val=float('-infinity')
        for j in range(i):
            max_val=max(max_val,price[j]+val[i-(j+1)])
        val[i]=max_val
    print(val)
    return val[n]
arr=[1, 5, 8, 9, 10, 17, 17, 20]
# arr=[3,5,8,9]
n=len(arr)
result=cutRod(arr,n)
print(result)
