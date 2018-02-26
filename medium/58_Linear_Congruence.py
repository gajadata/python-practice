# Have the function LinearCongruence(str) read the str parameter being passed which will be a linear congruence equation in the form: "ax = b (mod m)" Your goal is to solve for x and return the number of solutions to x. For example: if str is "32x = 8 (mod 4)" then your program should return 4 because the answers to this equation can be either 0, 1, 2, or 3. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.

import re

def LinearCongruence(s):
    m = re.match(r'(\d+)x\s*=\s*(\d+)\s*\(mod (\d+)\)', s)
    if m is None:
        return "Failed!"
    a, b, n = map(int, m.groups())
    while n != 0:
        a, n = n, a % n
    return a if b % a == 0 else 0

# keep this function call here  
print LinearCongruence(raw_input())