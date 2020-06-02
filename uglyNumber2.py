from heapq import heapify,heappop,heappush

def getUgly(n):
    primes=[2,3,5]
    if n<=0:
        return -1

    if n==1:
        return 1

    arr=[i for i in primes]
    heapify(arr)

    count=1
    while count<n:
        nextNumber=heappop(arr)
        if nextNumber!=arr[0]:
            count+=1
            for i in primes:
                heappush(arr,nextNumber*i)
    return nextNumber

if __name__ == '__main__':
    print(getUgly(1000))
