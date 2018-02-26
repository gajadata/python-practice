# Have the function ThreePoints(strArr) read the array of strings stored in strArr which will always contain 3 elements and be in the form: ["(x1,y1)", "(x2,y2)", "(x3,y3)"]. Your goal is to first create a line formed by the first two points (that starts from the first point and moves in the direction of the second point and that stretches in both directions through the two points), and then determine what side of the line point 3 is on. The result will either be right, left, or neither. For example: if strArr is ["(1,1)", "(3,3)", "(2,0)"] then your program should return the string right because the third point lies to the right of the line formed by the first two points. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def ThreePoints(strArr):
    p = map(eval, strArr)
    a = p[0][1] - p[1][1]
    b = p[1][0] - p[0][0]
    c = a * p[0][0] + b * p[0][1]
    
    if a * p[2][0] + b * p[2][1] - c > 0:
       return "left"
    if a * p[2][0] + b * p[2][1] - c < 0:
        return "right"
    return "neither"

# keep this function call here
print ThreePoints(raw_input())