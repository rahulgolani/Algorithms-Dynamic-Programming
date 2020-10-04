def getWaysToReachStairs(n):
    if n==0:
        return 1
    # if n==2:
    #     return 2
    result1,result2,result3=0,0,0
    if (n-1)>=0:
        result1=getWaysToReachStairs(n-1)
    if (n-2)>=0:
        result2=getWaysToReachStairs(n-2)
    if (n-3)>=0:
        result3=getWaysToReachStairs(n-3)
    return result1+result2+result3

if __name__ == '__main__':
    n=4
    print(getWaysToReachStairs(n))
