# Have the function MissingDigitII(str) take the str parameter, which will be a simple mathematical formula with three numbers, a single operator (+, -, *, or /) and an equal sign (=) and return the two digits that complete the equation. In two of the numbers in the equation, there will be a single ? character, and your program should determine what digits are missing and return them separated by a space. For example, if str is "38?5 * 3 = 1?595" then your program should output 6 1. 

# The ? character will always appear in both the first number and the last number in the mathematical expression. There will always be a unique solution. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.

def MissingDigitII(s): 
    ls, rs = s.split('=')
    for d1 in range(10):
        for d2 in range(10):
            if eval(ls.replace('?',str(d1))) == eval(rs.replace('?',str(d2))):
                return ' '.join(list(map(str, [d1,d2])))
    return '0 0'
    
# keep this function call here  
print MissingDigitII(raw_input())