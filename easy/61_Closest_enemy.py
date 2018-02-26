# Have the function ClosestEnemy(arr) take the array of numbers stored in arr and from the position in the array where a 1 is, return the number of spaces either left or right you must move to reach an enemy which is represented by a 2. For example: if arr is [0, 0, 1, 0, 0, 2, 0, 2] then your program should return 3 because the closest enemy (2) is 3 spaces away from the 1. The array will contain any number of 0's and 2's, but only a single 1. It may not contain any 2's at all as well, where in that case your program should return a 0. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def ClosestEnemy(arr):
    me = arr.index(1)
    res = len(arr)
    for i in xrange(0, len(arr)):
        if arr[i] == 2:
            res = min(res, abs(me - i))
    return 0 if res == len(arr) else res

# keep this function call here  
print ClosestEnemy(raw_input())