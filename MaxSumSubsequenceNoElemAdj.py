def Subsequence(arr):
    incl=arr[0]
    excl=0
    # print(incl)
    # print(excl)
    # print('\n')
    for i in range(1,len(arr)):
        #new_excl=max(incl,excl)
        new_incl=excl+arr[i]
        excl=max(incl,excl)
        incl=new_incl
        #excl=new_excl
        # print(incl)
        # print(excl)
        # print("\n")

    return max(incl,excl)
if __name__ == '__main__':
    arr=[5,5,10,100,10,5]
    result=Subsequence(arr)
    print(result)
# max(max(sum[i-1], sum[i-2] + arr[i]), arr[i] + arr[i-1] + sum[i-3])
