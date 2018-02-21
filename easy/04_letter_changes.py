# Have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm. 
# Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). 
# Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def LetterChanges(a_string):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    encoded_string = ''
    for letter in a_string.lower():
        if letter not in letters:
            encoded_string += letter
        elif letter == 'z':
            encoded_string += 'a'
        else:
          index = letters.index(letter)
          encoded_string += letters[index + 1]
    capitalized_encoded = ''

    for char in encoded_string:
        if char in 'aeiou':
            capitalized_encoded += char.upper()
        else:
            capitalized_encoded += char
    return capitalized_encoded


# # keep this function call here
# # to see how to enter arguments in Python scroll down
# print LetterChanges(raw_input())

# def LetterChanges(s): 
#     res = ''
#     for i in s:
#         if i.isalpha():
#             if i == 'z':
#                 i = 'a'
#             elif i == 'Z':
#                 i = 'A'
#             else:
#                 i = chr(ord(i) + 1)
#             if i in 'aeiou':
#                 i = i.upper()
#         res += i
#     return res

    
# # keep this function call here  
# print LetterChanges(raw_input())


