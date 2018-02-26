# Have the function StringZigzag(strArr) read the array of strings stored in strArr, which will contain two elements, the first some sort of string and the second element will be a number ranging from 1 to 6. The number represents how many rows to print the string on so that it forms a zig-zag pattern. For example: if strArr is ["coderbyte", "3"] then this word will look like the following if you print it in a zig-zag pattern with 3 rows: 


# Your program should return the word formed by combining the characters as you iterate through each row, so for this example your program should return the string creoebtdy. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.

def StringZigzag(a):
    w, l, c, check = a[0], [[] for n in range(int(a[1]))], 0, False
    for letter in w:
        l[c].append(w[0])
        w = w[1:]
        if check:
            c -= 1
            if c == 0:
                check = False
        else:
            c += 1
            if c == len(l) - 1:
                check = True
    new = ''
    for row in l:
        new += ''.join(row)
    return new
print StringZigzag(raw_input())