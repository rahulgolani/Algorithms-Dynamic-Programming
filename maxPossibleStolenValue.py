def getMaxStolenValueRec(hval):
    n=len(hval)
    if n==0:
        return 0
    if n==1:
        return hval[0]
    if n==2:
        return max(hval[0],hval[1])
    return getMaxStolenValueRecUtil(hval,n)

def getMaxStolenValue(hVal):
    n=len(hVal)
    if n==0:
        return 0
    if n==1:
        return hVal[0]
    if n==2:
        return max(hVal[0],hVal[1])
    lookup=[0]*n
    lookup[0]=hVal[0]
    lookup[1]=max(hVal[0],hVal[1])
    for i in range(2,n):
        lookup[i]=max(hVal[i]+lookup[i-2],lookup[i-1])
        # (include hval[i], exclude)
    return lookup[-1]

# def getMaxStolenValue(hVal):
#     incl=hVal[0]
#     excl=0
#     for i in range(1,len(hVal)):
#         newIncl=excl+hVal[i]
#         excl=max(incl,excl)
#         incl=newIncl
#     return max(incl,excl)

if __name__ == '__main__':
    hVal=[6, 7, 1, 3, 8, 2, 4]
    # hVal=[5, 3, 4, 11, 2]
    print(getMaxStolenValue(hVal))
