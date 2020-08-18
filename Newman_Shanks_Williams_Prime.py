def getNSWPrime(n):
    nsw=[0]*(n+1)
    nsw[0]=1
    nsw[1]=1
    for i in range(2,n+1):
        nsw[i]=2*nsw[i-1]+nsw[i-2]

    return nsw[n]

if __name__ == '__main__':
    n=6
    print(getNSWPrime(n))
