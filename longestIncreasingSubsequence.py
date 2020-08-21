def getLIS(arr):
    lookup=[1 for i in range(len(arr))]
    maxLength=1
    for i in range(1,len(arr)):
        for j in range(i):
            if arr[j]<arr[i]:
                lookup[i]=max(lookup[i],lookup[j]+1)
                if lookup[i]>maxLength:
                    maxLength=lookup[i]
    return maxLength


if __name__ == '__main__':
    # arr=[3,4,-1,0,6,2,3]
    arr=[10, 22, 9, 33, 21, 50, 41, 60, 80]
    result=getLIS(arr)
    print(result)
