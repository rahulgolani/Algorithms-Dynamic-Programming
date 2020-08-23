class Pair:
    def __init__(self,a,b):
        self.a=a
        self.b=b

def Chain(arr):
    n=len(arr)
    res=[1 for i in range(n)]
    for i in range(1,n):
        for j in range(i):
            if arr[j].b<arr[i].a:
                res[i]=max(res[i],res[j]+1)
    return max(res)

arr = [Pair(5, 24), Pair(15, 25), Pair(27, 40), Pair(50, 60)]
print(Chain(arr))
