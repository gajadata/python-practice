# Have the function SerialNumber(str) take the str parameter being passed and determine if it is a valid serial number with the following constraints: 

# 1. It needs to contain three sets each with three digits (1 through 9) separated by a period.
# 2. The first set of digits must add up to an even number.
# 3. The second set of digits must add up to an odd number.
# 4. The last digit in each set must be larger than the two previous digits in the same set.

# If all the above constraints are met within the string, the your program should return the string true, otherwise your program should return the string false. For example: if str is "224.315.218" then your program should return "true". 

# Use the Parameter Testing feature in the box below to test your code with different arguments.



def SerialNumber(s):
    if len(s.split('.')) != 3:
        return 'false'
    for i in range(len(s.split('.'))):
        if len(s.split('.')[i]) != 3:
            return 'false'
        if i == 0 and sum(int(c) for c in s.split('.')[i]) % 2 != 0:
            return 'false'
        if i == 1 and sum(int(c) for c in s.split('.')[i]) % 2 != 1:
            return 'false'
        if s.split('.')[i][2] < s.split('.')[i][1] or s.split('.')[i][2] < s.split('.')[i][0]:
            return 'false'
    return 'true'
print SerialNumber(raw_input())