# Some algorithms omit 0 to be the first number in the fibonacci sequence
'''
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        fib=[0]*(n+1)
        fib[1]=1
        for i in range(2,n+1):
            fib[i]=fib[i-1]+fib[i-2]
    return fib[-1]

result=fibonacci(5)

print(result)
'''

def fib(n):
    if n<0:
        return "Invalid input"
    a=0
    b=1
    if n==0:
        return a
    elif n==1:
        return b
    else:
        for i in range(2,n+1):
            c=a+b
            a=b
            b=c
    return c

if __name__ == '__main__':
    print(fib(6))
