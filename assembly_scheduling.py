def getMinBuildChassis(a,t,e,x):
    numOfStations=len(a[0])
    T1=[0]*(numOfStations)
    T2=[0]*numOfStations

    T1[0]=e[0]+a[0][0]
    T2[0]=e[1]+a[1][0]
    for i in range(1,numOfStations):
        T1[i]=min(T1[i-1]+a[0][i], T2[i-1]+t[1][i]+a[0][i])
        T2[i]=min(T2[i-1]+a[1][i], T1[i-1]+t[0][i]+a[1][i])

    print(T1)
    print(T2)

    return min(T1[numOfStations-1]+x[0],T2[numOfStations-1]+x[1])

if __name__ == '__main__':
    a = [[4, 5, 3, 2], [2, 10, 1, 4]]
    t = [[0, 7, 4, 5], [0, 9, 2, 8]]
    e = [10, 12]
    x = [18, 7]
    result=getMinBuildChassis(a,t,e,x)
    print(result)
