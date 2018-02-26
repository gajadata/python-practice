# Have the function SimplePassword(str) take the str parameter being passed and determine if it passes as a valid password that follows the list of constraints: 

# 1. It must have a capital letter.
# 2. It must contain at least one number.
# 3. It must contain a punctuation mark.
# 4. It cannot have the word "password" in the string.
# 5. It must be longer than 7 characters and shorter than 31 characters.

# If all the above constraints are met within the string, the your program should return the string true, otherwise your program should return the string false. For example: if str is "apple!M7" then your program should return "true". 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def SimplePassword(s):
    if len(s) not in xrange(8,31) or 'password' in s.lower():
        return 'false'
    upper = False
    digit = False
    punct = False
    for ch in s:
        if ch.isupper():
            upper = True
        if ch.isdigit():
            digit = True
        if not ch.isspace() and not ch.isalnum():
            punct = True
    return 'true' if upper and digit and punct else 'false'

# keep this function call here  
print SimplePassword(raw_input())