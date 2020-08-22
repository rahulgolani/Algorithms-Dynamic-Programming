def getMaxSubsequence(arr):
    lookup=[0]*len(arr)
    lookup[0]=arr[0]
    lookup[1]=arr[0]+arr[1]
    lookup[2]=max(lookup[1], arr[2]+arr[0],arr[2]+arr[1])
    for i in range(2,len(arr)):
        lookup[i]=max(lookup[i-1], arr[i]+lookup[i-2] ,arr[i]+arr[i-1]+lookup[i-3])
    # print(lookup)
    return lookup[len(arr)-1]
if __name__ == '__main__':
    arr=[3000, 2000, 1000, 3, 10]
    result=getMaxSubsequence(arr)
    print(result)
