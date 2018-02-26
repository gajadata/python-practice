# Have the function SimpleEvens(num) check whether every single number in the passed in parameter is even. If so, return the string true, otherwise return the string false. For example: if num is 4602225 your program should return the string false because 5 is not an even number. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def SimpleEvens(num):
    for i in str(num):
        if int(i) % 2 != 0:
            return 'false'
    return 'true'
print SimpleEvens(raw_input())