def getSuperUgly(n,primes):
    superUgly=[0]*(n)
    superUgly[0]=1
    index=[0]*len(primes)
    nextMultiple=[i for i in primes]
    for i in range(1,n):
        superUgly[i]=min(nextMultiple)
        for j in range(len(primes)):
            if nextMultiple[j]==superUgly[i]:
                index[j]+=1
                nextMultiple[j]=superUgly[index[j]]*primes[j]
    print(superUgly)
    return superUgly[-1]

if __name__ == '__main__':
    primes=[3, 5, 7, 11, 13]
    print(getSuperUgly(9,primes))
