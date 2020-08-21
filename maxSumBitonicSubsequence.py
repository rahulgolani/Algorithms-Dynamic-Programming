def MaxSumBitonicSubsequence(arr):
    lis=[arr[i] for i in range(len(arr))]
    lds=[arr[i] for i in range(len(arr))]

    for i in range(1,len(lis)):
        for j in range(i):
            if arr[j]<arr[i]:
                lis[i]=max(lis[i],lis[j]+arr[i])
    for i in range(len(lis)-2,-1,-1):
        for j in range(len(lis)-1,i,-1):
            if arr[j]<arr[i]:
                lds[i]=max(lds[i],lds[j]+arr[i])
    # print(lis)
    # print(lds)
    result=float('-infinity')
    for i in range(len(lis)):
        if lis[i]+lds[i]-arr[i]>result:
            result=lis[i]+lds[i]-arr[i]

    return result


if __name__ == '__main__':
    arr=[1,15,51,45,33,100,12,18,9]
    result=MaxSumBitonicSubsequence(arr)
    print(result)
