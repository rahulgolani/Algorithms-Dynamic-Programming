def getLongestSubsequence(arr):
    lookup=[1]*len(arr)
    maxLength=1
    for i in range(1,len(arr)):
        for j in range(i):
            if abs(arr[i]-arr[j])==1:
                lookup[i]=max(lookup[i],lookup[j]+1)
                if maxLength<lookup[i]:
                    maxLength=lookup[i]
    # print(lookup)
    return maxLength

if __name__ == '__main__':
    arr=[10, 9, 4, 5, 4, 8, 6]
    result=getLongestSubsequence(arr)
    print(result)
