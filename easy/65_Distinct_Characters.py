# Have the function DistinctCharacters(str) take the str parameter being passed and determine if it contains at least 10 distinct characters, if so, then your program should return the string true, otherwise it should return the string false. For example: if str is "abc123kkmmmm?" then your program should return the string false because this string contains only 9 distinct characters: a, b, c, 1, 2, 3, k, m, ? adds up to 9. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.

def DistinctCharacters(s): 
    return "true" if len(set(s)) > 9 else "false"

# keep this function call here  
print DistinctCharacters(raw_input())