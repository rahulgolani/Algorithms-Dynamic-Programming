class Area:
    def __init__(self,a,b):
        self.a=a
        self.b=b

def maxSurvivalTime(A,B,X,Y,Z,last,path):
    if A<=0 or B<=0:
        return 0
    cur=Area(A,B)
    for ele in path.keys():
        if cur.a==ele.a and cur.b==ele.b:
            return path[ele]
    if last==1:
        temp=1+max(maxSurvivalTime(A+Y.a,B+Y.b,X,Y,Z,2,path),maxSurvivalTime(A+Z.a,B+Z.b,X,Y,Z,3,path))
    elif last==2:
        temp=1+max(maxSurvivalTime(A+X.a,B+X.b,X,Y,Z,1,path),maxSurvivalTime(A+Z.a,B+Z.b,X,Y,Z,3,path))
    elif last==3:
        temp=1+max(maxSurvivalTime(A+X.a,B+X.b,X,Y,Z,1,path),maxSurvivalTime(A+Y.a,B+Y.b,X,Y,Z,2,path))
    path[cur]=temp
    return temp


def getMaxSurvialTime(A,B,X,Y,Z):
    if A<=0 or B<=0:
        return 0
    survivalPath=dict()
    return max(maxSurvivalTime(A+X.a,B+X.b,X,Y,Z,1,survivalPath),maxSurvivalTime(A+Y.a,B+Y.b,X,Y,Z,2,survivalPath),maxSurvivalTime(A+Z.a,B+Z.b,X,Y,Z,3,survivalPath))


A=20
B=8
X=Area(3, 2)
Y=Area(-5, -10)
Z=Area(-20, 5)
print(getMaxSurvialTime(A,B,X,Y,Z))
