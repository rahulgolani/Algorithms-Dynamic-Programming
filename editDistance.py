# recursive solution
def findMinEditDistanceRecUtil(a,b,n,m):
    if m==0:
        return n

    if n==0:
        return m

    if a[n-1]==b[m-1]:
        return findMinEditDistanceRecUtil(a,b,n-1,m-1)

    return 1+ min(findMinEditDistanceRecUtil(a,b,n-1,m),findMinEditDistanceRecUtil(a,b,n,m-1),findMinEditDistanceRecUtil(a,b,n-1,m-1))
    #remove , insert, replace


# dynamic programming solution
def findMinEditDistanceRec(a,b):
    n=len(a)
    m=len(b)
    return findMinEditDistanceRecUtil(a,b,n,m)

def findMinEditDistance(a,b):
    n=len(a)
    m=len(b)
    editDistance=[[0 for j in range(m+1)]for i in range(n+1)]
    for i in range(1,n+1):
        editDistance[i][0]=i
    for i in range(1,m+1):
        editDistance[0][i]=i
    for i in range(1,n+1):
        for j in range(1,m+1):
            if a[i-1]==b[j-1]:
                editDistance[i][j]=editDistance[i-1][j-1]
            else:
                editDistance[i][j]=min(editDistance[i-1][j],editDistance[i-1][j-1],editDistance[i][j-1])+1

    return editDistance[n][m]

if __name__ == '__main__':
    str1="sunday"
    str2="saturday"
    # str1='geek'
    # str2='gesek'
    print(findMinEditDistance(str1,str2))
    print(findMinEditDistanceRec(str1,str2))
