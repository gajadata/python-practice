# Have the function FormattedNumber(strArr) take the strArr parameter being passed, which will only contain a single element, and return the string true if it is a valid number that contains only digits with properly placed decimals and commas, otherwise return the string false. For example: if strArr is ["1,093,222.04"] then your program should return the string true, but if the input were ["1,093,22.04"] then your program should return the string false. The input may contain characters other than digits. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.

def FormattedNumber(strArr):
    nums = strArr[0].split('.')
    if len(nums) > 2:
        return "false"
    if len(nums) == 2:
        if not nums[1].isdigit():
            return "false"
    nums = nums[0].split(',')
    if nums[0][0] == '-':
        nums[0] = nums[0][1:]
    if len(nums[0]) > 3 or not nums[0].isdigit():
        return "false"
    for x in nums[1:]:
        if len(x) != 3 or not x.isdigit():
            return "false"
    return "true"

# keep this function call here  
print FormattedNumber(raw_input())