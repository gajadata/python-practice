# Have the function BoggleSolver(strArr) read the array of strings stored in strArr, which will contain 2 elements: the first element will represent a 4x4 matrix of letters, and the second element will be a long string of comma-separated words each at least 3 letters long, in alphabetical order, that represents a dictionary of some arbitrary length. For example: strArr can be: ["rbfg, ukop, fgub, mnry", "bog,bop,gup,fur,ruk"]. Your goal is to determine if all the comma separated words as the second parameter exist in the 4x4 matrix of letters. For this example, the matrix looks like the following: 

# r b f g 
# u k o p 
# f g u b 
# m n r y 

# The rules to make a word are as follows: 

# 1. A word can be constructed from sequentially adjacent spots in the matrix, where adjacent means moving horizontally, vertically, or diagonally in any direction.
# 2. A word cannot use the same location twice to construct itself. 

# The rules are similar to the game of Boggle. So for the example above, all the words exist in that matrix so your program should return the string true. If all the words cannot be found, then return a comma separated string of the words that cannot be found, in the order they appear in the dictionary. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


NN = 4
flist = []
def findword(da, w, v=[]):
    global NN
    nc = len(v)
    if w in flist: return
    if len(w)==nc:
        flist.append(w)
        return
    if nc==0:
        for i in range(NN): 
            for j in range(NN):
                if da[i][j]==w[nc]:
                    findword(da, w, v+[(i,j)])
    else:
        x, y = v[-1]
        for i in range(-1,2):
            for j in range(-1,2):
                if x+i<0 or y+j<0 or x+i>=NN or y+j>=NN: continue
                if (x+i, y+j) in v: continue
                if da[x+i][y+j]==w[nc]:
                    findword(da, w, v+[(x+i, y+j)])
    return
    
def BoggleSolver(sa): 
    words = sa[1].split(',')
    for wd in words: 
        findword(sa[0].replace(',', ' ').split(), wd, [])
    if len(words) == len(flist): 
        return 'true'
    return ','.join([x for x in words if x not in flist])
    
# keep this function call here  
print BoggleSolver(raw_input())