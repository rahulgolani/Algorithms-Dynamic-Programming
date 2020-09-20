def getMaxSum(arr,k):
    max_so_far=float('-infinity')
    max_ending_here=0
    start=0
    end=0
    s=0
    n=len(arr)
    for i in range(n*k):
        max_ending_here+=arr[i%n]
        if max_so_far<max_ending_here:
            max_so_far=max_ending_here
            start=s
            end=i
        if max_ending_here<0:
            max_ending_here=0
            s=i+1
    return max_so_far

if __name__ == '__main__':
    arr=[-1,10,20]
    k=2
    print(getMaxSum(arr,k))
