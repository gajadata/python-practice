# Have the function PlusMinus(num) read the num parameter being passed which will be a combination of 1 or more single digits, and determine if it's possible to separate the digits with either a plus or minus sign to get the final expression to equal zero. For example: if num is 35132 then it's possible to separate the digits the following way,
# 3 - 5 + 1 + 3 - 2, and this expression equals zero. Your program should return a string of the signs you used, so for this example your program should return -++-. If it's not possible to get the digit expression to equal zero, return the string not possible. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


import itertools
def PlusMinus(num):
    l = [i for i in str(num)]
    signs = itertools.product('+-', repeat=len(l)-1)
    for i in signs:
        m = list(i)
        n = []
        for x in range(len(l)):
            if x % 2 == 1:
                n.append(m[0])
                del m[0]
            n.append(l[x])
        if eval(''.join(n)) == 0:
            return ''.join(i)
    return 'not possible'
print PlusMinus(raw_input())