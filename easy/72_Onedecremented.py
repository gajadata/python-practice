# Have the function OneDecremented(num) count how many times a digit appears that is exactly one less than the previous digit. For example: if num is 5655984 then your program should return 2 because 5 appears directly after 6 and 8 appears directly after 9. The input will always contain at least 1 digit. Use the Parameter Testing feature in the box below to test your code with different arguments.


def OneDecremented(num):
    count = 0
    for i in range(len(list(str(num))))[1:]:
        if int(str(num)[i]) + 1 == int(str(num)[i-1]):
            count += 1
    return count
print OneDecremented(raw_input())