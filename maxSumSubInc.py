def maxSumSub(arr,n):
    result=[arr[i] for i in range(n)]
    maxResult=float('-infinity')
    for i in range(1,n):
        for j in range(i):
            if arr[j]<arr[i]:
                result[i]=max(result[i],result[j]+arr[i])
                if result[i]>maxResult:
                    maxResult=result[i]

    return maxResult

if __name__ == '__main__':
    arr=[4,6,1,3,8,4,6]
    print(maxSumSub(arr,len(arr)))
