# Have the function TrappingWater(arr) take the array of non-negative integers stored in arr, and determine the largest amount of water that can be trapped. The numbers in the array represent the height of a building (where the width of each building is 1) and if you imagine it raining, water will be trapped between the two tallest buildings. For example: if arr is [3, 0, 0, 2, 0, 4] then this array of building heights looks like the following picture if we draw it out: 

 

# Now if you imagine it rains and water gets trapped in this picture, then it'll look like the following (the x's represent water): 

 

# This is the most water that can be trapped in this picture, and if you calculate the area you get 10, so your program should return 10. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def TrappingWater(arr):
    traps = []
    for i in xrange(0, len(arr)):
        while len(traps) < arr[i]:
            traps.append([])
        for j in xrange(0, arr[i]):
            traps[j].append(i)
    result = 0
    for row in traps:
        for j in xrange(1, len(row)):
            result += (row[j] - row[j-1] - 1)
    return result

# keep this function call here  
print TrappingWater(raw_input())