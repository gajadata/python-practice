# Have the function LongestConsecutive(arr) take the array of positive integers stored in arr and return the length of the longest consecutive subsequence (LCS). An LCS is a subset of the original list where the numbers are in sorted order, from lowest to highest, and are in a consecutive, increasing order. The sequence does not need to be contiguous and there can be several different subsequences. For example: if arr is [4, 3, 8, 1, 2, 6, 100, 9] then a few consecutive sequences are [1, 2, 3, 4], and [8, 9]. For this input, your program should return 4 because that is the length of the longest consecutive subsequence. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


import itertools
def check(a):
    for i in range(1,len(a)):
        for m in range(i):
            if a[i] <= a[m]:
                return False
    return True
def S(s):
    b = [list(itertools.product([0,1], repeat=len(s)))]
    c = [[]]
    for i in range(len(b)):
        for l in range(len(b[i])):
            for x in range(len(b[i][l])):
                if b[i][l][x] == 1:
                    c[-1].append(s[x])
            c.append([])
    return c
def LongestConsecutive(a):
    c, m = S(a), []
    for i in c:
        if check(i):
            m.append(i)
    return len(max(m, key=len))
print LongestConsecutive(raw_input())