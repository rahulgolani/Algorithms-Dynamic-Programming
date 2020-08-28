def getMaxSumSubarraySize(arr):
    max_ending_here=0
    max_so_far=float('-infinity')
    start=0
    end=0
    s=0
    for i in range(len(arr)):
        max_ending_here+=arr[i]
        if max_so_far<max_ending_here:
            max_so_far=max_ending_here
            start=s
            end=i
        if max_ending_here<0:
            max_ending_here=0
            s=i+1
    return end-start+1

if __name__ == '__main__':
    arr=[-2, -3, 4, -1, -2, 1, 5, -3]
    print(getMaxSumSubarraySize(arr))
