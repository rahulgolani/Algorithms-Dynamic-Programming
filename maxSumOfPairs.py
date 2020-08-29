def getMaxSumOfPairs(arr,k):
    arr.sort()
    # print(arr)
    i=len(arr)-1
    result=[]
    while i>=0:
        # print(i)
        j=i-1
        matchFound=0
        # while j>=0:
        if j>=0 and (arr[i]-arr[j])<k:
            # print(arr[i],arr[j],arr[i]-arr[j])
            result.append((arr[j],arr[i]))
            matchFound=1
            i=j-1
            #break
        # else:
        #     break
            # j-=1
        if matchFound==0:
            i=i-1
    # print(result)
    maxSum=0
    for i in result:
        maxSum+=i[0]+i[1]
    return maxSum


if __name__ == '__main__':
    # arr=[3, 5, 10, 15, 17, 12, 9]
    arr=[5, 15, 10, 300]
    k=12

    print(getMaxSumOfPairs(arr,k))
