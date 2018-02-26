# Have the function LargestRowColumn(strArr) read the strArr parameter being passed which will be a 2D matrix of some arbitrary size filled with positive integers. Your goal is to determine the largest number that can be found by adding up three digits in the matrix that are within the same path, where being on the same path means starting from one of the elements and then moving either up, down, left, or right onto the next element without reusing elements. One caveat though, and that is when you calculate the sum of three digits, you should split the sum into two digits and treat the new digits as a row/column position in the matrix. So your goal is actually to find the sum of three digits that sums to the largest position in the matrix without going out of the bounds. For example: if strArr is ["345", "326", "221"] then this looks like the following matrix: 

# 3 4 5
# 3 2 6
# 2 2 1 

# The solution to this problem is to sum the bolded elements, 4 + 2 + 6, which equals 12. Then you take the solution, 12, and split it into two digits: 1 and 2 which represents row 1, column 2 in the matrix. This is the largest position you can get in the matrix by adding up 3 digits so your program should return 12. If you for example added up 4 + 5 + 6 in the matrix you would get 15 which is larger than 12, but row 1, column 5 is out of bounds. It's also not possible with the current matrix to sum to any of the following numbers: 20, 21, 22. If you find a sum that is only a single digit, you can treat that as row 0, column N where N is your sum. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def LargestRowColumn(strArr): 
    rows = range(0, len(strArr))
    columns = range(0, len(strArr[0]))
    steps = [[0,1],[-1,0],[0,-1],[1,0]]
    possible_answers = [10* x + y for x in rows for y in columns]
    answer = 0
    for i in rows:
        for j in columns:
            ways = [[[i + x[0], j + x[1]],[i + x[0] + y[0], j + x[1]+ y[1]]] for x in steps for y in steps if [i + x[0] + y[0], j + x[1]+ y[1]] != [i,j] and i + x[0] + y[0] in rows and j + x[1]+ y[1] in columns ]
            for way in ways:
                sums = int(strArr[i][j]) + int(strArr[way[0][0]][way[0][1]]) + int(strArr[way[1][0]][way[1][1]])
                if sums in possible_answers and sums > answer:
                    answer = sums
    return answer
    
# keep this function call here  
print LargestRowColumn(raw_input())