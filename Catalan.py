'''
Catalan numbers are a sum of catalan(i)*catalan(n-i-1)

Applications->
1)Number of possible Binary Search Trees with n keys.
2)Number of expressions containing n pairs of parentheses which are correctly
matched. For n = 3, possible expressions are ((())), ()(()), ()()(), (())(), (()()).
3)Number of ways a convex polygon of n+2 sides can split into triangles by connecting vertices.
4)Number of full binary trees (A rooted binary tree is full if every vertex has either two children or no children) with n+1 leaves.
5)Number of different Unlabeled Binary Trees can be there with n nodes.
6)The number of paths with 2n steps on a rectangular grid from bottom left, i.e.,
 (n-1, 0) to top right (0, n-1) that do not cross above the main diagonal.
7)Number of ways to insert n pairs of parentheses in a word of n+1 letters, e.g.,
 for n=2 there are 2 ways: ((ab)c) or (a(bc)). For n=3 there are 5 ways, ((ab)(cd)), (((ab)c)d), ((a(bc))d), (a((bc)d)), (a(b(cd))).
8)Number of noncrossing partitions of the set {1, …, 2n} in which every block is of size 2
9)Number of Dyck words of length 2n.
10)Number of ways to tile a stairstep shape of height n with n rectangles
11)Number of ways to connect the points on a circle disjoint chords.  This is similar to point 3 above.
12)Number of ways to form a “mountain ranges” with n upstrokes and n down-strokes that all stay above the original line.
The mountain range interpretation is that the mountains will never go below the horizon.
13)Number of stack-sortable permutations
14)the number of permutations with no three-term increasing subsequence
'''

'''
Recursive Solution

def catalan(n):
    if n<=1:
        return 1
    result=0
    for i in range(n):
        result+=catalan(i)*catalan(n-i-1)
    return result

if __name__ == '__main__':
    print(catalan(5))
'''

#DP Solution

def catalanNumber(n):
    catalan=[0 for i in range(n+1)]
    catalan[0]=1

    for i in range(1,n+1):
        for j in range(i):
            catalan[i]+=catalan[j]*catalan[i-j-1]

    print(catalan)
    return catalan[n]

result=catalanNumber(10)
print(result)
