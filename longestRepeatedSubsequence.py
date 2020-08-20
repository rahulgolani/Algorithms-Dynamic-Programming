def printSequence(lookup,a,n):
    i=n;j=n
    result=""
    while i>0 and j>0:
        if lookup[i][j]==lookup[i-1][j-1]+1:
            result+=a[i-1]
            i-=1
            j-=1
        elif lookup[i][j]==lookup[i-1][j]:
            i-=1
        else:
            j-=1
    print("".join(reversed(result)))

def lrs(a,b):
    n=len(a)
    lookup=[[0 for j in range(n+1)]for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if a[i-1]==b[j-1] and i!=j:
                lookup[i][j]=lookup[i-1][j-1]+1
            else:
                lookup[i][j]=max(lookup[i-1][j],lookup[i][j-1])
    printSequence(lookup,a,n)
    return lookup[n][n]

if __name__ == '__main__':
    str="aabebcdd"
    result=lrs(str,str)
    print(result)
