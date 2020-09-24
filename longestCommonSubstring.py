def getLongestCommonSubstring(a,b):
    n=len(a)
    m=len(b)
    lookup=[[0 for j in range(m+1)]for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if a[i-1]==b[j-1]:
                lookup[i][j]=lookup[i-1][j-1]+1
    result=float('-infinity')
    for i in range(1,n+1):
        for j in range(1,j+1):
            result=max(result,lookup[i][j])
    return result

if __name__ == '__main__':
    # str1="GeeksforGeeks"
    # str2="GeeksQuiz"
    # str1="abcdxyz"
    # str2="xyzabcd"
    str1="zxabcdezy"
    str2="yzabcdezx"
    print(getLongestCommonSubstring(str1,str2))
