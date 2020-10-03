def getSolutions(coeff,start,end,rhs):
    # print(start,end,rhs)
    if rhs==0:
        return 1
    result=0
    for i in range(start,end+1):
        if coeff[i]<=rhs:
            result+=getSolutions(coeff,i,end,rhs-coeff[i])
    return result

if __name__ == '__main__':
    coeff=[1,2]
    rhs=5
    n=len(coeff)
    print(getSolutions(coeff,0,n-1,rhs))
