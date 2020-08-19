def fibonacci(n):
    if n<0:
        print('Invalid input')
        return
    if n==0 or n==1:
        print(1)
        return
    a=0
    b=1
    print(a,end=" ")
    print(b,end=" ")
    for i in range(2,n+1):
        print(a+b,end=" ")
        # b = a + b
        # a = b - a
        a,b=b,a+b

if __name__ == '__main__':
    n=9
    fibonacci(n)
