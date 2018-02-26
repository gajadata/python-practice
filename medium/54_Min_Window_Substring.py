# Have the function MinWindowSubstring(strArr) take the array of strings stored in strArr, which will contain only two strings, the first parameter being the string N and the second parameter being a string K of some characters, and your goal is to determine the smallest substring of N that contains all the characters in K. For example: if strArr is ["aaabaaddae", "aed"] then the smallest substring of N that contains the characters a, e, and d is "dae" located at the end of the string. So for this example your program should return the string dae. 

# Another example: if strArr is ["aabdccdbcacd", "aad"] then the smallest substring of N that contains all of the characters in K is "aabd" which is located at the beginning of the string. Both parameters will be strings ranging in length from 2 to 50 characters and all of K's characters will exist somewhere in the string N. Both strings will only contains lowercase alphabetic characters. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.



def MinWindowSubstring(a):
    N, K, m = a[0], a[1], ['', len(a[0])]
    for y in range(len(K), len(N) + 1):
        for x in range(y):
            l, c = N[x:y], list(K[:])
            for i in l:
                if i in c:
                    c.remove(i)
            if len(c) == 0 and len(l) < m[1]:
                m[0], m[1] = l, len(l)
    return m[0]
print MinWindowSubstring(raw_input())