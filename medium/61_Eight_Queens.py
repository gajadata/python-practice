# Have the function EightQueens(strArr) read strArr which will be an array consisting of the locations of eight Queens on a standard 8x8 chess board with no other pieces on the board. The structure of strArr will be the following: ["(x,y)", "(x,y)", ...] where (x,y) represents the position of the current queen on the chessboard (x and y will both range from 1 to 8 where 1,1 is the bottom-left of the chessboard and 8,8 is the top-right). Your program should determine if all of the queens are placed in such a way where none of them are attacking each other. If this is true for the given input, return the string true otherwise return the first queen in the list that is attacking another piece in the same format it was provided. 

# For example: if strArr is ["(2,1)", "(4,2)", "(6,3)", "(8,4)", "(3,5)", "(1,6)", "(7,7)", "(5,8)"] then your program should return the string true. The corresponding chessboard of queens for this input is below (taken from Wikipedia). 

 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def check(a, b):
    return a[0] == b[0] or a[1] == b[1] or abs(a[0]-b[0]) == abs(a[1]-b[1])

def EightQueens(strArr):
    qns = map(eval, strArr)
    assert len(qns) == 8
    
    for i in xrange(0, len(qns)-1):
        for j in xrange(i+1, len(qns)):
            if check(qns[i], qns[j]):
                return strArr[i]
    return "true"

# keep this function call here
print EightQueens(raw_input())