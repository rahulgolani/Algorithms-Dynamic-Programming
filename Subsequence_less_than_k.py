# from itertools import combinations
#
# def getSubSequences(arr):
#     result=[]
#     letLen=pow(2,len(arr))
#     for i in range(letLen):
#         temp=""
#         for j in range(letLen):
#             if (i&pow(2,j)):
#                 temp+=str(arr[j])
#         if temp!="":
#             result.append(temp)
#     print(result)
#
# if __name__ == '__main__':
#     arr=[1,2,3,4]
#     getSubSequences(arr)


def productSubSeqCount(arr,k):
    n=len(arr)
    dp=[[0 for i in range(n+1)] for j in range(k+1)]
    for i in range(1,k+1):
        for j in range(1,n+1):
            dp[i][j]=dp[i][j-1]
            if arr[j-1]<=i and arr[j-1]>0:
                dp[i][j]+=dp[i//arr[j-1]][j-1]+1
    # for i in dp:
    #     print(i)
    return dp[k][n]

if __name__ == '__main__':
    arr=[1,2,3,4]
    k=5
    print(productSubSeqCount(arr,k))
