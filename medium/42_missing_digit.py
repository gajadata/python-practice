# Have the function MissingDigit(str) take the str parameter, which will be a simple mathematical formula with three numbers, a single operator (+, -, *, or /) and an equal sign (=) and return the digit that completes the equation. In one of the numbers in the equation, there will be an x character, and your program should determine what digit is missing. For example, if str is "3x + 12 = 46" then your program should output 4. The x character can appear in any of the three numbers and all three numbers will be greater than or equal to 0 and less than or equal to 1000000. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def MissingDigit(s):
  s = s.replace('=', '==')
  for x in xrange(0, 10):
    try:
      if eval(s.replace('x', str(x))):
        return x
    except:
      pass
  return None

# keep this function call here
print MissingDigit(raw_input())