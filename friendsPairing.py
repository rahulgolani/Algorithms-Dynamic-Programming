'''
def friendPairing(n):
    dp=[0 for i in range(n+1)]
    for i in range(2):
        dp[i]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+(i-1)*dp[i-2]
    return dp[n]

if __name__ == '__main__':
    print(friendPairing(4))
'''

def countFriendsPairings(n):
    a, b, c = 1, 1, 0;
    if n==0:
        return a
    if n==1:
        return b
    for i in range(2, n + 1):
        c = b + (i - 1) * a;
        a = b;
        b = c;
    return c;

# Driver code
n = 3;
print(countFriendsPairings(n));
