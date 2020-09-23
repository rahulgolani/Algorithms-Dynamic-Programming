# BFS based solution
'''
class Node:
    def __init__(self,val,distance):
        self.val=val
        self.distance=distance

def getMinSteps(n):
    queue=[]
    map={}
    start=Node(n,0)
    queue.append(start)
    map[start.val]=True
    while queue:
        current=queue.pop(0)
        if current.val==1:
            return current.distance
        if current.val%2==0 and current.val//2>0:
            if current.val//2 not in map:
                queue.append(Node(current.val//2,current.distance+1))
                map[current.val//2]=True
        if current.val%3==0 and current.val//3>0:
            if current.val//3 not in map:
                queue.append(Node(current.val//3,current.distance+1))
                map[current.val//3]=True
        if current.val-1>0:
            if current.val-1 not in map:
                queue.append(Node(current.val-1,current.distance+1))
                map[current.val-1]=True
    return -1

if __name__ == '__main__':
    n=10
    print(getMinSteps(n))
'''

# Recursive Solution
'''
def getMinSteps(n):
    if n==1:
        return 0
    if n<1:
        return -1

    if n%2==0 and n%3==0:
        result=min(getMinSteps(n//2),getMinSteps(n//3),getMinSteps(n-1))
    elif n%2==0:
        result=min(getMinSteps(n//2),getMinSteps(n-1))
    elif n%3==0:
        result=min(getMinSteps(n//3),getMinSteps(n-1))
    else:
        result=getMinSteps(n-1)

    if result!=-1:
        return 1+result
    return -1


if __name__ == '__main__':
    n=6
    print(getMinSteps(n))
'''

# Dynamic Programming Solution
def getMinSteps(n):
    lookup=[0]*(n+1)
    lookup[1]=0
    lookup[2]=1
    lookup[3]=1

    for i in range(4,n+1):
        if i%2==0 and i%3==0:
            lookup[i]=1+min(lookup[i//2],lookup[i//3],lookup[i-1])
        elif i%2==0:
            lookup[i]=1+min(lookup[i//2],lookup[i-1])
        elif i%3==0:
            lookup[i]=1+min(lookup[i//3],lookup[i-1])
        else:
            lookup[i]=1+lookup[i-1]
    # print(lookup)
    return lookup[n]


if __name__ == '__main__':
    n=10
    print(getMinSteps(n))
