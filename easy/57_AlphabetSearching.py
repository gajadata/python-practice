# Have the function AlphabetSearching(str) take the str parameter being passed and return the string true if every single letter of the English alphabet exists in the string, otherwise return the string false. For example: if str is "zacxyjbbkfgtbhdaielqrm45pnsowtuv" then your program should return the string true because every character in the alphabet exists in this string even though some characters appear more than once. Use the Parameter Testing feature in the box below to test your code with different arguments.

def AlphabetSearching(s):
    has = map(lambda x: chr(x) in s, range(ord('a'), ord('z') + 1))
    return "true" if all(has) else "false"

# keep this function call here  
print AlphabetSearching(raw_input())