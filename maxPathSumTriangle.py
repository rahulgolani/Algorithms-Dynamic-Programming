def getMaxPathSumTriangle(arr):
    for i in range(len(arr)-2,-1,-1):
        for j in range(i+1):
            arr[i][j]=max(arr[i][j]+arr[i+1][j],arr[i][j]+arr[i+1][j+1])
    # for i in range(len(arr)):
    #     print(arr[i])
    return arr[0][0]

if __name__ == '__main__':
    arr=[[3,0,0,0],[7,4,0,0],[2,4,6,0],[8,5,9,3]]
    print(getMaxPathSumTriangle(arr))
