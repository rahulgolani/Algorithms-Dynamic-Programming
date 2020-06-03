#Recursive Impementation for binomial coefficient
#helps to compute number of ways to select k objects from n objects, regardless of the order
'''
def BinomialCoeff(n,k):
    if k==0 or k==n:
        return 1
    return BinomialCoeff(n-1,k-1)+BinomialCoeff(n-1,k)

result=BinomialCoeff(5,2)
print(result)
'''
#Dynamic Programming approch to overcome overlapping subproblem

def BinomialCoeff(n,k):
    bin=[[0 for j in range(k+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(min(i,k)+1):
            if j==0 or j==i:
                bin[i][j]=1
            else:
                bin[i][j]=bin[i-1][j-1]+bin[i-1][j]
    #print(bin)
    return bin[n][k]

result=BinomialCoeff(5,3)
print(result)
