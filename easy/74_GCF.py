# Have the function GCF(arr) take the array of numbers stored in arr which will always contain only two positive integers, and return the greatest common factor of them. For example: if arr is [45, 12] then your program should return 3. There will always be two elements in the array and they will be positive integers. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def GCF(a):
    f = []
    for i in range(1, min(a[0], a[1]) + 1):
        if a[0] % i == 0 and a[1] % i == 0:
            f.append(i)
    if len(f) == 0:
        return 1
    return max(f)
print GCF(raw_input())