def getEndlessPoints(arr):
    n=len(arr)
    row=[[0 for j in range(n)]for i in range(n)]
    col=[[0 for j in range(n)]for i in range(n)]
    for i in range(n):
        isEndless=1
        for j in range(n-1,-1,-1):
            if arr[i][j]==0:
                isEndless=0
            row[i][j]=isEndless
    for i in range(n):
        isEndless=1
        for j in range(n-1,-1,-1):
            if arr[j][i]==0:
                isEndless=0
            col[j][i]=isEndless
    result=0
    for i in range(n):
        for j in range(n):
            if row[i][j] and col[i][j]:
                result+=1
    return result

if __name__ == '__main__':
    # arr=[[0,1,1],[1,1,0],[0,1,0]]
    arr=[[0,1,0],[1,1,1],[0,1,1]]
    print(getEndlessPoints(arr))
