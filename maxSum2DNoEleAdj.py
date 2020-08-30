def getMaxSum(arr):
    inc=max(arr[0][0],arr[1][0])
    exc=0
    for i in range(1,len(arr[0])):
        exc_new=max(inc,exc)
        inc=exc+max(arr[0][i],arr[1][i])
        exc=exc_new
        # print(exc,inc)
    return max(inc,exc)

if __name__ == '__main__':
    arr=[[1,4,5],[2,0,0]]
    print(getMaxSum(arr))
