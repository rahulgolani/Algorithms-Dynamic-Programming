# Given an array of n distinct elements, find length of the largest subset such that every pair in the subset is such that the larger element of the pair is divisible by smaller element.

def getLargestDivisiblePair(arr,n):
    arr.sort()
    dp=[0 for i in range(n)]
    dp[n-1]=1#for the largest number
    for i in range(n-2,-1,-1):
        maxx=0
        for j in range(i+1,n):
            if arr[j]%arr[i]==0:
                maxx=max(dp[j],maxx)
        dp[i]=maxx+1
    return max(dp)


if __name__ == '__main__':
    arr=[10,5,3,15,20]
    n=len(arr)
    result=getLargestDivisiblePair(arr,n)
    print(result)
