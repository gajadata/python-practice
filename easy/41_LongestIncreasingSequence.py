# Have the function LongestIncreasingSequence(arr) take the array of positive integers stored in arr and return the length of the longest increasing subsequence (LIS). A LIS is a subset of the original list where the numbers are in sorted order, from lowest to highest, and are in increasing order. The sequence does not need to be contiguous or unique, and there can be several different subsequences. For example: if arr is [4, 3, 5, 1, 6] then a possible LIS 
# is [3, 5, 6], and another is [1, 6]. For this input, your program should return 3 because that is the length of the longest increasing subsequence. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def LongestIncreasingSequence(a): 
   if len(a)<2: return len(a)
   return max(LongestIncreasingSequence(a[1:]), 1+LongestIncreasingSequence([x for x in a if x>a[0]]))
    
# keep this function call here  
print LongestIncreasingSequence(raw_input())


# Another Solutuion :

# def LongestIncreasingSequence(arr): 

#     incr = range(max(arr) + 1)
    
#     M = [[0]*(len(arr) + 1) for i in xrange(len(incr))]
    
#     for i in xrange(1, len(M)):
#         for j in xrange(1, len(M[0])):
#             M[i][j] = M[i-1][j-1] + 1 if arr[j-1] == incr[i] else max(M[i][j-1], M[i-1][j]) 
            
#     return M[-1][-1]
    
# # keep this function call here  
# print LongestIncreasingSequence(raw_input())