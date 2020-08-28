def getMinPathSumTriangle(arr):
    for i in range(len(arr)-2,-1,-1):
        for j in range(i+1):
            arr[i][j]=arr[i][j]+min(arr[i+1][j],arr[i+1][j+1])
    return arr[0][0]

if __name__ == '__main__':
    arr=[[2,0,0,0],[3,7,0,0],[8,5,6,0],[6,1,9,3]]
    print(getMinPathSumTriangle(arr))
