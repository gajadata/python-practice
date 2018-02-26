# Have the function NumberStream(str) take the str parameter being passed which will contain the numbers 2 through 9, and determine if there is a consecutive stream of digits of at least N length where N is the actual digit value. If so, return the string true, otherwise return the string false. For example: if str is "6539923335" then your program should return the string true because there is a consecutive stream of 3's of length 3. The input string will always contain at least one digit. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def NumberStream(s):
    streams = ['2' * 2, '3' * 3, '4' * 4, '5' * 5, '6' * 6, '7' * 7, '8' * 8, '9' * 9]
    for i in streams:
        if i in s:
            return 'true'
    return 'false'
print NumberStream(raw_input())