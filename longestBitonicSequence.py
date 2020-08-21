def getLongestBitonicSequence(arr):
    lis=[1]*len(arr)
    lds=[1]*len(arr)
    for i in range(1,len(arr)):
        for j in range(i):
            if arr[j]<arr[i]:
                lis[i]=max(lis[i],lis[j]+1)
    for i in range(len(arr)-2,-1,-1):
        for j in range(len(arr)-1,i-1,-1):
            if arr[j]<arr[i]:
                lds[i]=max(lds[i],lds[j]+1)
    # print(lis)
    # print(lds)
    result=float('-infinity')
    for i in range(len(lis)):
        if lis[i]+lds[i]-1>result:
            result=lis[i]+lds[i]-1
    return result

if __name__ == '__main__':
    arr=[2,-1,4,3,5,-1,3,2]
    result=getLongestBitonicSequence(arr)
    print(result)
