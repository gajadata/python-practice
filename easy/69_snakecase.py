# Have the function SnakeCase(str) take the str parameter being passed and return it in proper snake case format where each word is lowercased and separated from adjacent words via an underscore. The string will only contain letters and some combination of delimiter punctuation characters separating each word. 

# For example: if str is "BOB loves-coding" then your program should return the string bob_loves_coding. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.

import re
def SnakeCase(s):
    return '_'.join(re.findall(r"[\w']+", s.lower()))
print SnakeCase(raw_input())