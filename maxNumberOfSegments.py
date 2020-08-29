# Simple Recursive Solution
'''
def maxSegments(n,a,b,c):
    if n==0:
        return 0
    if n<0:
        return -1
    res=max(maxSegments(n-a,a,b,c),maxSegments(n-b,a,b,c),maxSegments(n-c,a,b,c))
    if res>=0:
        return 1+res
    else:
        return -1

if __name__ == '__main__':
    n=7
    a=5
    b=2
    c=5
    print(maxSegments(n,a,b,c))
'''
# Dynamic Programming Solution

def maxSegments(n,a,b,c):
    lookup=[-1]*(n+1)
    lookup[0]=0
    for i in range(n+1):
        if lookup[i]!=-1:
            if (i+a)<=n:
                lookup[i+a]=max(lookup[i+a],lookup[i]+1)
            if (i+b)<=n:
                lookup[i+b]=max(lookup[i+b],lookup[i]+1)
            if (i+c)<=n:
                lookup[i+c]=max(lookup[i+c],lookup[i]+1)
    # print(lookup)
    return lookup[n]

if __name__ == '__main__':
    n=7
    a=5
    b=2
    c=5
    print(maxSegments(n,a,b,c))
