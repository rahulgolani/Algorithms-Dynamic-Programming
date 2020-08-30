def getMaxWeightPath(arr):
    rows=len(arr)
    cols=len(arr[0])
    lookup=[[0 for j in range(cols)] for i in range(rows)]
    for i in range(cols):
        lookup[rows-1][i]=arr[rows-1][i]
    for i in range(rows-2,-1,-1):
        for j in range(cols):
            if j==cols-1:
                lookup[i][j]=arr[i][j]+lookup[i+1][j]
            else:
                lookup[i][j]=arr[i][j]+max(lookup[i+1][j],lookup[i+1][j+1])
    return lookup[0][0]

if __name__ == '__main__':
    arr=[[4, 2 ,3 ,4 ,1],[2 , 9 ,1 ,10 ,5],[15, 1 ,3 , 0 ,20],[16 ,92, 41, 44 ,1],[8, 142, 6, 4, 8]]
    print(getMaxWeightPath(arr))
