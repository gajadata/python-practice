# Have the function BitwiseTwo(strArr) take the array of strings stored in strArr, which will only contain two strings of equal length that represent binary numbers, and return a final binary string that performed the bitwise AND operation on both strings. A bitwise AND operation places a 1 in the new string where there is a 1 in both locations in the binary strings, otherwise it places a 0 in that spot. For example: if strArr is ["10111", "01101"] then your program should return the string "00101" 

# Use the Parameter Testing feature in the box below to test your code with different arguments.

def BitwiseTwo(strArr): 
   return '{0:b}'.format(int(strArr[0], 2) & int(strArr[1], 2))

# keep this function call here
print BitwiseTwo(raw_input())

