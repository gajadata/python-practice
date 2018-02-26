# Have the function BinaryReversal(str) take the str parameter being passed, which will be a positive integer, take its binary representation, reverse that string of bits, and then finally return the new reversed string in decimal form. For example: if str is "47" then the binary version of this integer is 00101111. Your program should reverse this binary string which then becomes: 11110100 and then finally return the decimal version of this string, which is 244. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def BinaryReversal(string): 
    binary = "{0:b}".format(int(string))[::-1]
    binary += '0' * (7 - (len(binary) - 1) % 8)
    return str(int(binary, 2))


# keep this function call here  
print BinaryReversal(raw_input())