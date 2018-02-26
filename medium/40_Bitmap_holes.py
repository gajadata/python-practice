# Have the function BitmapHoles(strArr) take the array of strings stored in strArr, which will be a 2D matrix of 0 and 1's, and determine how many holes, or contiguous regions of 0's, exist in the matrix. A contiguous region is one where there is a connected group of 0's going in one or more of four directions: up, down, left, or right. For example: if strArr is ["10111", "10101", "11101", "11111"], then this looks like the following matrix: 

# 1 0 1 1 1
# 1 0 1 0 1
# 1 1 1 0 1
# 1 1 1 1 1 

# For the input above, your program should return 2 because there are two separate contiguous regions of 0's, which create "holes" in the matrix. You can assume the input will not be empty. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def FillHole(m, i0, j0):
    q = [(i0, j0)]
    while len(q) > 0:
        i, j = q.pop()
        m[i][j] = '1';
        if i+1 < len(m) and m[i+1][j] == '0':
            q.append((i+1, j))
        if j+1 < len(m[i]) and m[i][j+1] == '0':
            q.append((i, j+1))
        if i > 0 and m[i-1][j] == '0':
            q.append((i-1, j))
        if j > 0 and m[i][j-1] == '0':
            q.append((i, j-1))

def BitmapHoles(strArr):
    count = 0
    m = [list(x) for x in strArr]
    for i in xrange(0, len(m)):
        for j in xrange(0, len(m[i])):
            if m[i][j] == '0':
                count += 1
                FillHole(m, i, j)
    return count

# keep this function call here
print BitmapHoles(raw_input())