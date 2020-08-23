def getLongestSubsequence(arr,i,k):
    arrNew=[0]*(i+2)
    for i in range(i+1):
        arrNew[i]=arr[i]
    arrNew[-1]=arr[k]
    lookup=[arrNew[i] for i in range(len(arrNew))]
    # maxSum=float('-infinity')
    for i in range(1,len(arrNew)):
        for j in range(i):
            if arr[j]<arr[i]:
                lookup[i]=max(lookup[i],lookup[j]+arrNew[i])
                # if lookup[i]>maxSum:
                #     maxSum=lookup[i]
    return lookup[-1]

if __name__ == '__main__':
     arr=[1, 101, 2, 3, 100, 4, 5]
     i=4
     k=6
     result=getLongestSubsequence(arr,i,k)
     print(result)
