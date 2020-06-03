def tile(n):
    if n==1:  #2*1 only one way vertically
        return 1
    if n==2: #2*2 2 ways either put both vertically 2*1, 2*1 or both horizontally 1*2, 1*2
        return 2
    ways=[0]*(n+1)
    # ways[0]=1
    ways[1]=1
    ways[2]=2
    for i in range(3,n+1):
        ways[i]=ways[i-1]+ways[i-2]
    return ways[n]

n=3
print(tile(n))
