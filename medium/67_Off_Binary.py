# Have the function OffBinary(strArr) read the array of strings stored in strArr, which will contain two elements, the first will be a positive decimal number and the second element will be a binary number. Your goal is to determine how many digits in the binary number need to be changed to represent the decimal number correctly (either 0 change to 1 or vice versa). For example: if strArr is ["56", "011000"] then your program should return 1 because only 1 digit needs to change in the binary number (the first zero needs to become a 1) to correctly represent 56 in binary. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def OffBinary(strArr): 
    a, b = strArr
    a = bin(int(a))[2:]
    diff = len(a) - len(b)
    if diff > 0:
        b = ('0' * diff) + b
    elif diff < 0:
        a = ('0' * diff) + a
    return sum(map(lambda x, y: x != y, a, b))

# keep this function call here  
print OffBinary(raw_input())