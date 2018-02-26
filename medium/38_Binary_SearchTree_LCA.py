# Have the function BinarySearchTreeLCA(strArr) take the array of strings stored in strArr, which will contain 3 elements: the first element will be a binary search tree with all unique values in a preorder traversal array, the second and third elements will be two different values, and your goal is to find the lowest common ancestor of these two values. For example: if strArr is ["[10, 5, 1, 7, 40, 50]", "1", "7"] then this tree looks like the following: 

 

# For the input above, your program should return 5 because that is the value of the node that is the LCA of the two nodes with values 1 and 7. You can assume the two nodes you are searching for in the tree will exist somewhere in the tree. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def BinarySearchTreeLCA(strArr):
    tree, u, v = map(eval, strArr)
    lca = 0
    u, v = sorted([u, v])
    while not u <= tree[lca] <= v:
        if u < tree[lca]:
            lca += 1
        else:
            tmp = lca + 1
            while tree[tmp] < tree[lca]:
                tmp += 1
            lca = tmp
    return tree[lca]

# keep this function call here  
print BinarySearchTreeLCA(raw_input())