# BFS based solution
'''
def getSum(num):
    queue=[]
    total=0
    n=len(num)
    map={}
    for i in range(n):
        queue.append(int(num[i]))
        map[int(num[i])]=i
    while queue:
        current=queue.pop(0)
        total+=current
        lastDigitIndex=map[current%10]
        if lastDigitIndex<n-1:
            queue.append(current*10+int(num[lastDigitIndex+1]))
    return total

if __name__ == '__main__':
    n="1234"
    # n="421"
    print(getSum(n))
'''

'''
Example : num = "1234"
sumofdigit[0] = 1 = 1
sumofdigit[1] = 2 + 12  = 14
sumofdigit[2] = 3 + 23  + 123 = 149
sumofdigit[3] = 4 + 34  + 234 + 1234  = 1506
Result = 1670
Now we can get the relation between sumofdigit values and can solve the question iteratively. Each sumofdigit can be represented in terms of previous value as shown below,

For above example,
sumofdigit[3] = 4 + 34 + 234 + 1234
           = 4 + 30 + 4 + 230 + 4 + 1230 + 4
           = 4*4 + 10*(3 + 23 +123)
           = 4*4 + 10*(sumofdigit[2])
In general,
sumofdigit[i]  =  (i+1)*num[i] + 10*sumofdigit[i-1]
'''

def getSum(num):
    n=len(num)
    lookup=[0]*n
    lookup[0]=int(num[0])
    result=lookup[0]
    for i in range(1,n):
        lookup[i]=(i+1)*int(num[i])+10*lookup[i-1]
        result+=lookup[i]

    return result

if __name__ == '__main__':
    n="1234"
    # n="421"
    print(getSum(n))
