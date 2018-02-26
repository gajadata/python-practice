# Have the function MatrixPath(strArr) take the strArr parameter being passed which will be a 2D matrix of 0 and 1's of some arbitrary size, and determine if a path of 1's exists from the top-left of the matrix to the bottom-right of the matrix while moving only in the directions: up, down, left, and right. If a path exists your program should return the string true, otherwise your program should return the number of locations in the matrix where if a single 0 is replaced with a 1, a path of 1's will be created successfully. If a path does not exist and you cannot create a path by changing a single location in the matrix from a 0 to a 1, then your program should return the string not possible. For example: if strArr is ["11100", "10011", "10101", "10011"] then this looks like the following matrix: 

# 1 1 1 0 0
# 1 0 0 1 1
# 1 0 1 0 1
# 1 0 0 1 1 

# For the input above, a path of 1's from the top-left to the bottom-right does not exist. But, we can change a 0 to a 1 in 2 places in the matrix, namely at locations: [0,3] or [1,2]. So for this input your program should return 2. The top-left and bottom-right of the input matrix will always be 1's. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


dir = [(-1,0),(1,0),(0,-1),(0,1)]
def MatrixPath(sa): 
    NX, NY = len(sa[0]), len(sa)
    pa = [[int(sa[y][x]) for x in range(NX)] for y in range(NY)] 
    C = 1
    for p in [(0,0), (NY-1,NX-1)]:
        q = [p]
        C += 1
        while q:
            y,x = q.pop(0)
            if (pa[y][x]!=1): continue
            pa[y][x] = C
            for dx,dy in dir:
                if x+dx<0 or y+dy<0 or x+dx>=NX or y+dy>=NY: 
                    continue
                if pa[y+dy][x+dx]==1: 
                    q.append((y+dy,x+dx))
    if pa[NY-1][NX-1] == 2:
        return 'true'
    cnt = 0
    for y in range(NY):
        for x in range(NX):
            if pa[y][x]!=0: continue
            b2,b3 = False, False
            for dx,dy in dir:
                if x+dx<0 or y+dy<0 or x+dx>=NX or y+dy>=NY: continue
                if pa[y+dy][x+dx]==2: b2 = True
                if pa[y+dy][x+dx]==3: b3 = True
            if b2 and b3: cnt += 1    
    return cnt if cnt else 'not possible'
    
# keep this function call here  
print MatrixPath(raw_input())