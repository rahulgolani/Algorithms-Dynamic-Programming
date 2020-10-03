def getNumber(n):
    lookup=[None]*(n+1)
    lookup[0]=0
    lookup[1]=1
    for i in range(2,n+1):
        if i%2==0:
            lookup[i]=lookup[i//2]
        else:
            lookup[i]=lookup[(i-1)//2]+lookup[(i+1)//2]
    return lookup[n]

if __name__ == '__main__':
    n=9
    result=getNumber(n)
    print(result)
