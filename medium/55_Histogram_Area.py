# Have the function HistogramArea(arr) read the array of non-negative integers stored in arr which will represent the heights of bars on a graph (where each bar width is 1), and determine the largest area underneath the entire bar graph. For example: if arr is [2, 1, 3, 4, 1] then this looks like the following bar graph: 

 

# You can see in the above bar graph that the largest area underneath the graph is covered by the x's. The area of that space is equal to 6 because the entire width is 2 and the maximum height is 3, therefore 2 * 3 = 6. Your program should return 6. The array will always contain at least 1 element. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def HistogramArea(arr): 
    res = 0
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr) + 1):
            res = max(res, (j - i) * min(arr[i:j]))
    return res

# keep this function call here  
print HistogramArea(raw_input())