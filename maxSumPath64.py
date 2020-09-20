def getMaxSumPath(arr):
    n=len(arr)
    lookup=[[-1 for j in range(n)]for i in range(n)]
    for i in range(n):
        lookup[n-1][i]=arr[n-1][i]
    for i in range(n-2,-1,-1):
        for j in range(n):
            if j==0:
                lookup[i][j]=max(lookup[i+1][j],lookup[i+1][j+1])+arr[i][j]
            elif j==n-1:
                lookup[i][j]=max(lookup[i+1][j-1],lookup[i+1][j])+arr[i][j]
            else:
                lookup[i][j]=max(lookup[i+1][j-1],lookup[i+1][j],lookup[i+1][j+1])+arr[i][j]
    # print(lookup)
    return max(lookup[0])

if __name__ == '__main__':
    arr=[[4, 2, 3, 4],[2, 9, 1, 10],[15, 1, 3, 0],[16, 92, 41, 44]]
    print(getMaxSumPath(arr))
