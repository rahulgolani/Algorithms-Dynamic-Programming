def printSequence(lookup,a,b,m,n):
    i=m;j=n
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

def getLongestCommonSubsequence(a,b):
    lookup=[[0 for j in range(len(b)+1)]for i in range(len(a)+1)]
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            if a[i-1]==b[j-1]:
                lookup[i][j]=lookup[i-1][j-1]+1
            else:
                lookup[i][j]=max(lookup[i-1][j],lookup[i][j-1])
    # for i in range(len(lookup)):
    #     print(lookup[i])
    printSequence(lookup,a,b,len(a),len(b))
    return lookup[len(a)][len(b)]


if __name__ == '__main__':
    str1="abcdaf"
    str2="abcbf"
    # str1="AGGTAB"
    # str2="GXTXAYB"
    result=getLongestCommonSubsequence(str1,str2)
    print(result)
