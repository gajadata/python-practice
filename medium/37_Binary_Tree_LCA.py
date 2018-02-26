# Have the function BinaryTreeLCA(strArr) take the array of strings stored in strArr, which will contain 3 elements: the first element will be a binary tree with all unique values in a format similar to how a binary heap is implemented with NULL nodes at any level represented with a #, the second and third elements will be two different values, and your goal is to find the lowest common ancestor of these two values. For example: if strArr is 
# ["[12, 5, 9, 6, 2, 0, 8, #, #, 7, 4, #, #, #, #]", "6", "4"] then this tree looks like the following: 

 

# For the input above, your program should return 5 because that is the value of the node that is the LCA of the two nodes with values 6 and 4. You can assume the two nodes you are searching for in the tree will exist somewhere in the tree. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def LCA(u, v):
    path = []
    while 1:
        if u == v:
            return u
        if u in path:
            return u
        if v in path:
            return v
        path += [u, v]
        u, v = (u - 1) // 2, (v - 1) // 2

def BinaryTreeLCA(strArr):
    tree, u, v = strArr
    tree = eval(tree.replace('#', 'None'))
    u = tree.index(int(u))
    v = tree.index(int(v))
    return tree[LCA(u, v)]

# keep this function call here  
print BinaryTreeLCA(raw_input())