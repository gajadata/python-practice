Have the function StringPeriods(str) take the str parameter being passed and determine if there is some substring K that can be repeated N > 1 times to produce the input string exactly as it appears. Your program should return the longest substring K, and if there is none it should return the string -1. 

For example: if str is "abcababcababcab" then your program should return abcab because that is the longest substring that is repeated 3 times to create the final string. Another example: if str is "abababababab" then your program should return ababab because it is the longest substring. If the input string contains only a single character, your program should return the string -1. 

Use the Parameter Testing feature in the box below to test your code with different arguments.


def StringPeriods(s):
    choice = []
    for i in range(1, len(s) - 1):
        l = s[:i+1]
        x = int(len(s) / (i + 1))
        n = ''
        for i in range(x):
            n += l
        if n == s:
            choice.append(l)
    if len(choice) == 0:
        return '-1'
    return max(choice, key=len)
print StringPeriods(raw_input())