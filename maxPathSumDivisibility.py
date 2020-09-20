def getMaxPathSum(arr):
    path=[None]*(len(arr)+1)
    for i in range(1,len(path)):
        path[i]=arr[i-1]
    # print(path)
    for i in range(1,(len(path)//2)+1):
        for j in range(i+i,len(path),i):
            path[j]=max(path[j],path[i]+arr[j-1])
    return path

if __name__ == '__main__':
    arr=[2, 3, 1, 4, 6, 5]
    result=getMaxPathSum(arr)
    for i in range(1,len(result)):
        print(result[i],end=" ")
