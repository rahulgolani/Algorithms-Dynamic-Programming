'''
You are given a bag of size W kg and you are provided costs of packets different weights of oranges in array cost[] where cost[i] is basically cost of ‘i’ kg packet of oranges. Where cost[i] = -1 means that ‘i’ kg packet of orange is unavailable

Find the minimum total cost to buy exactly W kg oranges and if it is not possible to buy exactly W kg oranges then print -1. It may be assumed that there is infinite supply of all available packet types.
'''

def getMinCost(arr,w):
    wt=[]
    val=[]
    for i in range(len(arr)):
        if arr[i]!=-1:
            wt.append(i+1)
            val.append(arr[i])
    # print(wt)
    # print(val)
    n=len(wt)
    lookup=[[0 for j in range(w+1)]for i in range(n+1)]
    for i in range(1,w+1):
        lookup[0][i]=float('infinity')
    for i in range(1,n+1):
        lookup[i][0]=0
    for i in range(1,n+1):
        for j in range(1,w+1):
            if wt[i-1]<=j:
                lookup[i][j]=min(lookup[i-1][j],val[i-1]+lookup[i][j-wt[i-1]])
            else:
                lookup[i][j]=lookup[i-1][j]
    if lookup[n][w]==float('infinity'):
        return -1
    return lookup[n][w]


if __name__ == '__main__':
    arr=[20, 10, 4, 50, 100]
    # arr=[-1, -1, 4, 5, -1]
    w=5
    print(getMinCost(arr,w))
