#Recursive Solution
# def elementSequence(m,n):
#     if m<n:
#         return 0
#     if n==0:
#         return 1
#
#     return elementSequence(m//2,n-1)+elementSequence(m-1,n)
#
# if __name__ == '__main__':
#     m=5
#     n=4
#     print(elementSequence(m,n))


# Dynamic Programming Solution
def elementSequence(m,n):
    lookup=[[0 for j in range(n+1)]for i in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if i<j:
                lookup[i][j]=0
            elif j==1:
                lookup[i][j]=i
            else:
                lookup[i][j]=lookup[i-1][j]+lookup[i//2][j-1]
    # print(lookup)
    return lookup[m][n]

if __name__ == '__main__':
    m=10
    n=4
    result=elementSequence(m,n)
    print(result)
