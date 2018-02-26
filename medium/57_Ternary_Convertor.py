# Have the function TernaryConverter(num) take the num parameter being passed, which will always be a positive integer, and convert it into a ternary representation. For example: if num is 12 then your program should return 110. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def TernaryConverter(n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return int(''.join(reversed(nums)))
print TernaryConverter(raw_input())