# Have the function CamelCase(str) take the str parameter being passed and return it in proper camel case format where the first letter of each word is capitalized (excluding the first letter). The string will only contain letters and some combination of delimiter punctuation characters separating each word. 

# For example: if str is "BOB loves-coding" then your program should return the string bobLovesCoding. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def CamelCase(s):
    out = ''
    capital = False
    for ch in s:
        if ch.isalpha():
            out += ch.upper() if capital else ch.lower()
            capital=False
        elif len(out) > 0:
            capital=True
    return out

# keep this function call here  
print CamelCase(raw_input())