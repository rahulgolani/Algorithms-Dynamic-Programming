'''
def checkSquareMatrix(arr,i,j,k):
    for m in range(k):
        for n in range(k):
            if arr[i+m][j+n]==0:
                return False
    return True

def getMaxSquareMatrix(arr):
    rows=len(arr)
    cols=len(arr[0])
    maxSize=1
    for i in range(rows):
        for j in range(cols):
            if arr[i][j]==1:
                count=1
                k=j+1
                while k<cols and arr[i][k]==1:
                    count+=1
                    k+=1
                if count>maxSize:
                    if checkSquareMatrix(arr,i,j,count):
                        maxSize=count
    print(maxSize)

if __name__ == '__main__':
    arr=[[0,1,1,0,1],[1,1,0,1,0],[0,1,1,1,0],[1,1,1,1,0],[1,1,1,1,1],[0,0,0,0,0]]
    getMaxSquareMatrix(arr)
'''

# Dynamic Programming Solution
# Algorithm:
# Let the given binary matrix be M[R][C]. The idea of the algorithm is to construct an auxiliary size matrix S[][] in which each entry S[i][j] represents size of the square sub-matrix with all 1s including M[i][j] where M[i][j] is the rightmost and bottommost entry in sub-matrix.
#
# 1) Construct a sum matrix S[R][C] for the given M[R][C].
#      a)    Copy first row and first columns as it is from M[][] to S[][]
#      b)    For other entries, use following expressions to construct S[][]
#          If M[i][j] is 1 then
#             S[i][j] = min(S[i][j-1], S[i-1][j], S[i-1][j-1]) + 1
#          Else /*If M[i][j] is 0*/
#             S[i][j] = 0
# 2) Find the maximum entry in S[R][C]
# 3) Using the value and coordinates of maximum entry in S[i], print
#    sub-matrix of M[][]

def getMaxSquareMatrix(arr):
    rows=len(arr)
    cols=len(arr[0])
    maxSize=1
    lookup=[[0 for j in range(cols)]for i in range(rows)]
    for i in range(rows):
        lookup[i][0]=arr[i][0]
    for i in range(cols):
        lookup[0][i]=arr[0][i]
    for i in range(1,rows):
        for j in range(1,cols):
            if arr[i][j]==1:
                lookup[i][j]=min(lookup[i-1][j],lookup[i][j-1],lookup[i-1][j-1])+1
                if lookup[i][j]>maxSize:
                    maxSize=lookup[i][j]
    return maxSize


if __name__ == '__main__':
    arr=[[0,1,1,0,1],[1,1,0,1,0],[0,1,1,1,0],[1,1,1,1,0],[1,1,1,1,1],[0,0,0,0,0]]
    print(getMaxSquareMatrix(arr))
