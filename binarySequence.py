def binarySequence(n,diff):
    if n==1 and diff==0:
        return 2
    if n==1 and abs(diff)==1:
        return 1
    if abs(diff)>n:
        return 0

    return 2*binarySequence(n-1,diff)+binarySequence(n-1,diff-1)+binarySequence(n-1,diff+1)

if __name__ == '__main__':
    n=2
    print(binarySequence(n,0))
