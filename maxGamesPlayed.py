def getMaxGames(n):
    lookup=[0 for i in range(n)]
    lookup[0]=1
    # lookup[match]=player
    lookup[1]=2
    i=1
    while lookup[i]<=n:
        i+=1
        lookup[i]=lookup[i-1]+lookup[i-2]

    return i-1


if __name__ == '__main__':
    n=4
    print(getMaxGames(n))
