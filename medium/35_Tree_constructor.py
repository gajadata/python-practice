# Have the function TreeConstructor(strArr) take the array of strings stored in strArr, which will contain pairs of integers in the following format: (i1,i2), where i1 represents a child node in a tree and the second integer i2 signifies that it is the parent of i1. For example: if strArr is ["(1,2)", "(2,4)", "(7,2)"], then this forms the following tree: 

 

# which you can see forms a proper binary tree. Your program should, in this case, return the string true because a valid binary tree can be formed. If a proper binary tree cannot be formed with the integer pairs, then return the string false. All of the integers within the tree will be unique, which means there can only be one node in the tree with the given integer value. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def TreeConstructor(strArr): 
    tree = {}
    parent = {}
    for pair in strArr:
        x, p = eval(pair)
        tree.setdefault(p, []).append(x)
        if x in parent:
            return "false"
        parent[x] = p
    
    root = set()
    for x in tree:
        if len(tree[x]) > 2:
            return "false"
        p = parent.get(x, None)
        while p:
            x = p
            p = parent.get(x, None)
        root.add(x)
    return "true" if len(root) == 1 else "false"

# keep this function call here
print TreeConstructor(raw_input())