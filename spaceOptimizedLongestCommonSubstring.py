def getLongestCommonSubstring(a,b):
    n=len(a)
    m=len(b)
    lookup=[[0 for j in range(m+1)]for i in range(2)]
    row=bool
    result=float('-infinity')
    for i in range(n):
        row=i&1
        for j in range(1,m+1):
            if a[i]==b[j-1]:
                lookup[row][j]=lookup[1-row][j-1]+1
                result=max(result,lookup[row][j])

    return result

if __name__ == '__main__':
    # str1="abcdxyz"
    # str2="xyzabcd"
    str1="GeeksforGeeks"
    str2="GeeksQuiz"
    print(getLongestCommonSubstring(str1,str2))
