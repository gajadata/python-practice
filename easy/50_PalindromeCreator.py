# Have the function PalindromeCreator(str) take the str parameter being passed and determine if it is possible to create a palindromic string of at least 3 characters by removing 1 or 2 characters. For example: if str is "abjchba" then you can remove the characters jc to produce "abhba" which is a palindrome. For this example your program should return the two characters that were removed with no delimiter and in the order they appear in the string, so jc. If 1 or 2 characters cannot be removed to produce a palindrome, then return the string not possible. If the input string is already a palindrome, your program should return the string palindrome. 

# The input will only contain lowercase alphabetic characters. Your program should always attempt to create the longest palindromic substring by removing 1 or 2 characters (see second sample test case as an example). The 2 characters you remove do not have to be adjacent in the string. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.



def PalindromeCreator(s):
    if s == s[::-1]:
        return "palindrome"

    for i in range(0, len(s)):
        for j in range(i, len(s)):
            news = s[0:i] + s[i+1:j] + s[j+1:]
            if len(news) > 2 and news == news[::-1]:
                return s[i] + s[j] if i != j else s[i]
    return "not possible"

# keep this function call here  
print PalindromeCreator(raw_input())