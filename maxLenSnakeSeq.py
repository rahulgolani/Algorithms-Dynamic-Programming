def getMaxLenSnakeSequence(arr):
    rows=len(arr)
    cols=len(arr[0])
    # initalizing with 1 length sequence
    result=[[1 for j in range(cols)]for i in range(rows)]

    maxLen=1
    maxRow=0
    maxCol=0
    for i in range(rows):
        for j in range(cols):
            #if we can check left or above
            if i or j:
                # checking above
                if i>0 and abs(arr[i][j]-arr[i-1][j])==1:
                    result[i][j]=max(result[i][j],result[i-1][j])+1
                    # adjusting values if a move found
                    if result[i][j]>maxLen:
                        maxLen=result[i][j]
                        maxRow=i
                        maxCol=j
                # checking left
                if j>0 and abs(arr[i][j]-arr[i][j-1])==1:
                    result[i][j]=max(result[i][j],result[i][j-1])+1
                    # adjusting values if move found
                    if result[i][j]>maxLen:
                        maxLen=result[i][j]
                        maxRow=i
                        maxCol=j
    print(result,maxLen,maxRow,maxCol)
    printSequence(result,maxRow,maxCol)


def printSequence(arr,i,j):
    path=[]
    path.append((i,j))
    while arr[i][j]!=1:
        if i>0 and arr[i][j]-1==arr[i-1][j]:
            path.append((i-1,j))
            i=i-1
        elif j>0 and arr[i][j]-1==arr[i][j-1]:
            path.append((i,j-1))
            j=j-1
    path=list(reversed(path))
    print(path)

if __name__ == '__main__':
    arr=[[9, 6, 5, 2], [8, 7, 6, 5], [7, 3, 1, 6], [1, 1, 1, 7]]
    getMaxLenSnakeSequence(arr)
