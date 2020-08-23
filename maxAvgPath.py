def getMaxAvgPath(arr):
    lookup=[[0 for j in range(len(arr))]for i in range(len(arr))]
    n=len(arr)
    for i in range(n):
        for j in range(n):
            if i==0 and j==0:
                lookup[i][j]=arr[i][j]
            elif i==0:
                lookup[i][j]=arr[i][j]+lookup[i][j-1]
            elif j==0:
                lookup[i][j]=arr[i][j]+lookup[i-1][j]
            else:
                lookup[i][j]=arr[i][j]+max(lookup[i-1][j],lookup[i][j-1])
    return lookup[n-1][n-1]/((2*n)-1)

if __name__ == '__main__':
    # arr=[[1, 2, 3],[4,5,6],[7,8,9]]
    arr=[[1, 2, 3], [6, 5, 4], [7, 3, 9]]
    result=getMaxAvgPath(arr)
    print(result)
