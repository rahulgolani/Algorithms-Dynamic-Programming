def paintingFence(n,k):
    mod=1000000007
    total=[0]*(n+1)
    total[1]=k
    same=0
    diff=k
    for i in range(2,n+1):
        same=diff
        diff=total[i-1]*(k-1)
        total[i]=(same+diff)#%mod

    return total[n]

n,k=15,6
print(paintingFence(n,k))
