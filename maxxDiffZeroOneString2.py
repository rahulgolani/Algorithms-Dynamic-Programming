def getMaxDiff(s,n):
    arr=[None]*n
    for i in range(n):
        if s[i]=='0':
            arr[i]=1
        else:
            arr[i]=-1
    # print(arr)
    max_ending_here=0
    max_till_now=float('-infinity')
    s=0
    start=0
    end=0
    for i in range(n):
        max_ending_here+=arr[i]
        if max_ending_here>max_till_now:
            max_till_now=max_ending_here
            start=s
            end=i
        if max_ending_here<0:
            max_ending_here=0
            s=i+1
    return (max_till_now,start,end)

if __name__ == '__main__':
    s="11000010001"
    # s="1111"
    result=getMaxDiff(s,len(s))
    if result[0]==-1:
        print("Not Applicable")
    else:
        print(f"Max Difference = {result[0]} starting from {result[1]} ending at {result[2]}")
