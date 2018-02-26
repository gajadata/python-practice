# Have the function PalindromeSwapper(str) take the str parameter being passed and determine if a palindrome can be created by swapping two adjacent characters in the string. If it is possible to create a palindrome, then your program should return the palindrome, if not then return the string -1. The input string will only contain alphabetic characters. For example: if str is "rcaecar" then you can create a palindrome by swapping the second and third characters, so your program should return the string racecar which is the final palindromic string. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.

def PalindromeSwapper(s):
    for i in range(len(s) - 1):
        if s[:i] + s[i + 1] + s[i] + s[i + 2:] == (s[:i] + s[i + 1] + s[i] + s[i + 2:])[::-1]:
            return s[:i] + s[i + 1] + s[i] + s[i + 2:]
    return '-1'
print PalindromeSwapper(raw_input())