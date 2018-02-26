# Have the function PreorderTraversal(strArr) take the array of strings stored in strArr, which will represent a binary tree with integer values in a format similar to how a binary heap is implemented with NULL nodes at any level represented with a #. Your goal is to return the pre-order traversal of the tree with the elements separated by a space. For example: if strArr is ["5", "2", "6", "1", "9", "#", "8", "#", "#", "#", "#", "4", "#"] then this tree looks like the following tree: 

 

# For the input above, your program should return the string 5 2 1 9 6 8 4 because that is the pre-order traversal of the tree. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


# Have the function PreorderTraversal(strArr) take the array of strings stored in strArr, which will represent a binary tree with integer values in a format similar to how a binary heap is implemented with NULL nodes at any level represented with a #. Your goal is to return the pre-order traversal of the tree with the elements separated by a space. For example: if strArr is ["5", "2", "6", "1", "9", "#", "8", "#", "#", "#", "#", "4", "#"] then this tree looks like the following tree: 

 

# For the input above, your program should return the string 5 2 1 9 6 8 4 because that is the pre-order traversal of the tree. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def PreorderTraversal(strArr): 
    if len(strArr) < 4:
        answer = ""
        for e in strArr:
            if e != "#":
                answer += " " + e
        return answer[1:]  
    left, right, left_leafs, right_leafs, right_leafs_last, count, index = [], [], 0, 0, 0, 0, 1
    while index < len(strArr) and count < 40:
        count += 1
        for i in range(0, len(strArr)):
            left_leafs *= 2
            left_leafs_last = left_leafs
            right_leafs *= 2
            right_leafs_2_last = right_leafs_last
            right_leafs_last = right_leafs
            for k in range(0,2**i - left_leafs_last):
                if index < len(strArr):
                   left.append(strArr[index])    
                   if strArr[index] == "#":
                        left_leafs += 1
                index += 1
            for k in range(0,2**i-right_leafs_last):
                if index< len(strArr):
                   right.append(strArr[index])  
                   if strArr[index]  == "#":
                        right_leafs += 1
                index += 1
    return (strArr[0] + " " + PreorderTraversal(left) +" "+ PreorderTraversal(right)).replace("  ", " ")
print PreorderTraversal(raw_input())