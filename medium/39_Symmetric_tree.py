# Have the function SymmetricTree(strArr) take the array of strings stored in strArr, which will represent a binary tree, and determine if the tree is symmetric (a mirror image of itself). The array will be implemented similar to how a binary heap is implemented, except the tree may not be complete and NULL nodes on any level of the tree will be represented with a #. For example: if strArr is ["1", "2", "2", "3", "#", "#", "3"] then this tree looks like the following: 

 

# For the input above, your program should return the string true because the binary tree is symmetric. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def SymmetricTree(strArr): 
    i, j = 1, 3
    while i < len(strArr):
        if j > len(strArr):
            strArr += ['#'] * (len(strArr)-j)
        for k in range(0, (j-i) >> 1):
            if strArr[i+k] != strArr[j-k-1]:
                return "false"
        i, j = 2 * i + 1, 2 * j + 1
    return "true"

# keep this function call here  
print SymmetricTree(raw_input())