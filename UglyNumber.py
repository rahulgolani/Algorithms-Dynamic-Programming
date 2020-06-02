#Ugly number is a number which is a multiple of only 2, 3 or 5

#iterative solution->
'''
def maxDivide(a,b):
    while a%b==0:
        a=a/b
    return a

def isUgly(no):
    no=maxDivide(no,2)
    no=maxDivide(no,3)
    no=maxDivide(no,5)
    return True if no==1 else False

def uglyNumber(n):
    i=1
    count=1
    ugly=[1]
    while count<n:
        i+=1
        if isUgly(i):
            count+=1
            ugly.append(i)
    print(ugly)
    print(ugly[-1])

uglyNumber(150)
'''

#Dynamic Programming solution->

def uglyNumber(n):
    ugly=[0]*(n+1) #initialize an array of size n
    ugly[0]=1 #set first ugly number as 1 by convention
    i2=i3=i5=0 #initialize 3 indices
    next_multiple_of_2=2
    next_multiple_of_3=3
    next_multiple_of_5=5

    for i in range(1,n+1):
        ugly[i]=min(next_multiple_of_2,next_multiple_of_3,next_multiple_of_5)
        if ugly[i]==next_multiple_of_2:
            i2+=1
            next_multiple_of_2=ugly[i2]*2
        if ugly[i]==next_multiple_of_3:
            i3+=1
            next_multiple_of_3=ugly[i3]*3
        if ugly[i]==next_multiple_of_5:
            i5+=1
            next_multiple_of_5=ugly[i5]*5
        #print(ugly)

    return ugly[n]

result=uglyNumber(10)
print(result)
