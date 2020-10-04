# recursive solution
# def Score(steps,n,score):
#     if score==0:
#         return 1
#     if score<0:
#         return 0
#     if score>0 and n<=0:
#         return 0
#     return Score(steps,n-1,score)+Score(steps,n,score-steps[n-1])
#
# if __name__ == '__main__':
#     steps=[3,5,10]
#     score=20
#     print(Score(steps,len(steps),score))

#dp solution
def Score(n):
    dp=[0]*(n+1)
    dp[0]=1
    for i in range(3,n+1):
        dp[i]+=dp[i-3]
    for i in range(5,n+1):
        dp[i]+=dp[i-5]
    for i in range(10,n+1):
        dp[i]+=dp[i-10]
    # print(dp)
    return dp[n]
if __name__ == '__main__':
    result=Score(20)
    print(result)
