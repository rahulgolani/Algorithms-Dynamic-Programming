def getMinCostPath(arr):
    n=len(arr)
    lookup=[[-1 for j in range(n)]for i in range(n)]
    lookup[0][0]=arr[0][0]
    for i in range(1,n):
        lookup[0][i]=arr[0][i]+lookup[0][i-1]
    for i in range(1,n):
        lookup[i][0]=arr[i][0]+lookup[i-1][0]
    for i in range(1,n):
        for j in range(1,n):
            lookup[i][j]=min(lookup[i-1][j],lookup[i-1][j-1],lookup[i][j-1])+arr[i][j]
    return lookup[n-1][n-1]

if __name__ == '__main__':
    arr=[[1,2,3],[4,8,2],[1,5,3]]
    print(getMinCostPath(arr))
