# Have the function LargestPair(num) take the num parameter being passed and determine the largest double digit number within the whole number. For example: if num is 4759472 then your program should return 94 because that is the largest double digit number. The input will always contain at least two positive digits. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def LargestPair(num):
    snum = str(num)
    res = 0
    for i in range(1, len(snum)):
        res = max(res, int(snum[i-1:i+1]))
    return res

# keep this function call here  
print LargestPair(raw_input())