# Have the function SwapCase(str) take the str parameter and swap the case of each character. 
# For example: if str is "Hello World" the output should be hELLO wORLD. Let numbers and symbols stay the way they are. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.

def SwapCase(str): 

    # code goes here 
    j = []
    for i in str:
        if i.isalpha():
            if i.islower():
                i = i.upper()
            elif i.isupper():
                i = i.lower()
        j.append(i)
        
    return ''.join(j)
    
# keep this function call here  
print SwapCase(raw_input())