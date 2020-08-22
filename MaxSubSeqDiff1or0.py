def getLongestSubsequence(arr):
    lookup=[1]*len(arr)
    maxLength=1
    for i in range(1,len(arr)):
        for j in range(i):
            if abs(arr[i]-arr[j])==1 or abs(arr[i]-arr[j])==0:
                lookup[i]=max(lookup[i],lookup[j]+1)
                if maxLength<lookup[i]:
                    maxLength=lookup[i]
    # print(lookup)
    return maxLength

if __name__ == '__main__':
    # arr=[2, 5, 6, 3, 7, 6, 5, 8]
    arr=[-2, -1, 5, -1, 4, 0, 3]
    result=getLongestSubsequence(arr)
    print(result)
