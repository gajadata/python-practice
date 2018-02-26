# Have the function MultiplicativePersistence(num) take the num parameter being passed which will always be a positive integer and return its multiplicative persistence which is the number of times you must multiply the digits in num until you reach a single digit. For example: if num is 39 then your program should return 3 because 3 * 9 = 27 then 2 * 7 = 14 and finally 1 * 4 = 4 and you stop at 4. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.

def MultiplicativePersistence(num): 
    if num < 10 : return 0
    nump = 1
    for i in [int(x) for x in str(num)]:
        nump *= i
    return 1 + MultiplicativePersistence(nump) 

    
# keep this function call here  
print MultiplicativePersistence(raw_input())