# Have the function MaxSubarray(arr) take the array of numbers stored in arr and determine the largest sum that can be formed by any contiguous subarray in the array. For example, if arr is [-2, 5, -1, 7, -3] then your program should return 11 because the sum is formed by the subarray [5, -1, 7]. Adding any element before or after this subarray would make the sum smaller. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def MaxSubarray(arr):
  last_s = arr[0]
  max_s = last_s
  for x in arr[1:]:
    if x > last_s + x:
       last_s = x
    else:
       last_s += x
    max_s = max(max_s, last_s)
  return max_s

# keep this function call here
print MaxSubarray(raw_input())