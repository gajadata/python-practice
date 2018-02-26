# Have the function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers, letters, and question marks, and check if there are exactly 3 question marks between every pair of two numbers that add up to 10. If so, then your program should return the string true, otherwise it should return the string false. If there aren't any two numbers that add up to 10 in the string, then your program should return false as well. 

# For example: if str is "arrb6???4xxbl5???eee5" then your program should return true because there are exactly 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def QuestionsMarks(s):
    qnum = 0
    dig = 0
    has_10 = False
    for ch in s:
        if ch.isdigit():
            if int(ch) + dig == 10:
                if qnum != 3:
                    return 'false'
                has_10 = True
            dig = int(ch)
            qnum = 0
        elif ch == '?':
            qnum += 1
    return 'true' if has_10 else 'false'

# keep this function call here  
print QuestionsMarks(raw_input())