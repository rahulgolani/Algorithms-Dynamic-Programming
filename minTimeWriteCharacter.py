# BFS based solution
'''
class Node:
    def __init__(self,val,time):
        self.val=val
        self.time=time

def getMinTime(n,iTime,rTime,cTime):
    queue=[]
    map={}
    start=Node(1,1)
    map[start.val]=True
    queue.append(start)
    while queue:
        current=queue.pop(0)
        if current.val==n:
            return current.time
        if (current.val+1) not in map:
            queue.append(Node(current.val+1,current.time+iTime))
            map[current.val+1]=True
        if (current.val-1) not in map and (current.val-1)>0:
            queue.append(Node(current.val-1,current.time+rTime))
            map[current.val-1]=True
        if (current.val*2) not in map:
            queue.append(Node(current.val*2,current.time+cTime))
            map[current.val*2]=True
    return -1

if __name__ == '__main__':
    n=9
    insertTime=1
    removalTime=2
    copyTime=1
    print(getMinTime(n,insertTime,removalTime,copyTime))
'''


def getMinTime(n,iTime,rTime,cTime):
    if n==0:
        return 0
    if n==1:
        return 1
    lookup=[0]*(n+1)
    lookup[1]=1
    for i in range(2,n+1):
        if i%2==0:
            lookup[i]=min(lookup[i-1]+iTime,lookup[i//2]+cTime)
        else:
            lookup[i]=min(lookup[i-1]+iTime,lookup[(i+1)//2]+cTime+rTime)
    return lookup[n]

if __name__ == '__main__':
    n=9
    insertTime=1
    removalTime=2
    copyTime=1
    print(getMinTime(n,insertTime,removalTime,copyTime))
