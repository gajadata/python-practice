# Have the function RemoveBrackets(str) take the str string parameter being passed, which will contain only the characters "(" and ")", and determine the minimum number of brackets that need to be removed to create a string of correctly matched brackets. For example: if str is "(()))" then your program should return the number 1. The answer could potentially be 0, and there will always be at least one set of matching brackets in the string. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def RemoveBrackets(s):
    a, c = 0, 0
    for i in s:
        if i == '(':
            c += 1
        elif i == ')':
            c -= 1
        if c < 0:
            a += abs(c)
            c = 0
    if c > 0:
        a += c
    return a
print RemoveBrackets(raw_input())