# Have the function TwoSum(arr) take the array of integers stored in arr, and determine if any two numbers (excluding the first element) in the array can sum up to the first element in the array. For example: if arr is [7, 3, 5, 2, -4, 8, 11], then there are actually two pairs that sum to the number 7: [5, 2] and [-4, 11]. Your program should return all pairs, with the numbers separated by a comma, in the order the first number appears in the array. Pairs should be separated by a space. So for the example above, your program would return: 5,2 -4,11 

# If there are no two numbers that sum to the first element in the array, return -1 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def TwoSum(arr): 
    s, arr = arr[0], arr[1:]
    res = []
    i = 0
    while i < len(arr) - 1:
        x, y = arr[i], s - arr[i]
        if y in arr[i+1:]:
            res.append(str(x) + ',' + str(y))
            del arr[i]
            del arr[arr.index(y)]
        else:
            i += 1
    return ' '.join(res) if len(res) > 0 else -1

# keep this function call here  
print TwoSum(raw_input())