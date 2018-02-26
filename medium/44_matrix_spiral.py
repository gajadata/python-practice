# Have the function MatrixSpiral(strArr) read the array of strings stored in strArr which will represent a 2D N matrix, and your program should return the elements after printing them in a clockwise, spiral order. You should return the newly formed list of elements as a string with the numbers separated by commas. For example: if strArr is "[1, 2, 3]", "[4, 5, 6]", "[7, 8, 9]" then this looks like the following 2D matrix: 

# 1 2 3
# 4 5 6
# 7 8 9 

# So your program should return the elements of this matrix in a clockwise, spiral order which is: 1,2,3,6,9,8,7,4,5 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def MatrixSpiral(strArr): 
    strArr = [eval(x) for x in strArr]
    res = []
    def slasher(arr, start):
        if len(arr) == 0: 
            return None
        last_row = len(arr)-1
        last_column = len(arr[0])-1
        if start == 'top left':
            for i in arr[0]: res.append(i)
            del arr[0]
            slasher(arr, 'top right')
        elif start == 'bottom right':
            for i in arr[last_row][::-1]: res.append(i)
            del arr[last_row]    
            slasher(arr, 'bottom left')
        elif start == 'top right':
            for i in range(last_row+1): 
                res.append(arr[i][last_column])
                del arr[i][last_column]
            slasher(arr, 'bottom right')    
        elif start == 'bottom left':
            for i in range(last_row+1)[::-1]: 
                res.append(arr[i][0])
                del arr[i][0]
            slasher(arr, 'top left') 
    slasher(strArr, 'top left') 
    res = [str(x) for x in res]
    return ','.join(res) 
print MatrixSpiral(raw_input())