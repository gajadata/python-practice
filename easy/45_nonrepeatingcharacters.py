# Have the function NonrepeatingCharacter(str) take the str parameter being passed, which will contain only alphabetic characters and spaces, and return the first non-repeating character. For example: if str is "agettkgaeee" then your program should return k. The string will always contain at least one character and there will always be at least one non-repeating character. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def NonrepeatingCharacter(str): 
    for i in str:
        if str.count(i) == 1 :
            return i

    # code goes here 
    return str
    
# keep this function call here  
print NonrepeatingCharacter(raw_input())