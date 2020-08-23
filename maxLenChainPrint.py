class Pair:
    def __init__(self,a,b):
        self.a=a
        self.b=b

def printMaxLenChain(arr):
    lookup=[[] for i in range(len(arr))]
    lookup[0].append(arr[0])
    for i in range(1,len(arr)):
        for j in range(i):
            if arr[j].b<arr[i].a and len(lookup[j])>len(lookup[i]):
                lookup[i]=lookup[j]
        lookup[i].append(arr[i])

    chain=[]
    for x in lookup:
        if len(x)>len(chain):
            chain=x
    for i in chain:
        print(f"({i.a},{i.b}) ",end=" ")

if __name__ == '__main__':
    arr=[Pair(5, 24), Pair(15, 25), Pair(27, 40), Pair(50, 60)]
    printMaxLenChain(arr)
