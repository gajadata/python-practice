# Using the Python language, have the function EvenPairs(str) take the str parameter being passed and determine if a pair of adjacent even numbers exists anywhere in the string. If a pair exists, return the string true, otherwise return false. For example: if str is "f178svg3k19k46" then there are two even numbers at the end of the string, "46" so your program should return the string true. Another example: if str is "7r5gg812" then the pair is "812" (8 and 12) so your program should return the string true. 


def EvenPairs(s):
    first_found = False
    for ch in s:
        if ch.isdigit():
            n = int(ch)
            if not first_found:
                first_found = (n % 2 == 0)
            elif n % 2 == 0:
                return 'true'
        else:
            first_found = False
    return 'false'

# keep this function call here  
print EvenPairs(raw_input())