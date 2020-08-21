def getLongestCommonSubsequence(a,b):
    m=len(a)
    n=len(b)
    lookup=[[0 for j in range(n+1)] for i in range(2)]
    bi=bool
    for i in range(m):
        bi=i&1
        for j in range(1,n+1):
            if a[i]==b[j-1]:
                lookup[bi][j]=lookup[1-bi][j-1]+1
            else:
                lookup[bi][j]=max(lookup[1-bi][j],lookup[bi][j-1])
    return lookup[bi][n]

if __name__ == '__main__':
    str1="abcdaf"
    str2="abcbf"
    # str1="AGGTAB"
    # str2="GXTXAYB"
    result=getLongestCommonSubsequence(str1,str2)
    print(result)
