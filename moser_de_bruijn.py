def moser_de_bruijn(n):
    s=[0,1]
    for i in range(2,n+1):
        if i%2==0:
            s.append(4*s[i//2])
        else:
            s.append(4*s[i//2]+1)
    print(s)

if __name__ == '__main__':
    n=10
    moser_de_bruijn(n)
