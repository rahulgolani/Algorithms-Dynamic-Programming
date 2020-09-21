def findMinJumpsToReachEnd(arr):
    n=len(arr)
    jumps=[float('infinity')]*n
    parent=[-1]*n
    jumps[0]=0
    for i in range(1,n):
        for j in range(i):
            if arr[j]+j>=i:
                if jumps[j]+1<jumps[i]:
                    jumps[i]=jumps[j]+1
                    parent[i]=j
                # jumps[i]=min(jumps[i],jumps[j]+1)
    # print(parent)
    return jumps[-1]

if __name__ == '__main__':
    arr=[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    print(findMinJumpsToReachEnd(arr))
