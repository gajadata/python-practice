# Have the function RectangleArea(strArr) take the array of strings stored in strArr, which will only contain 4 elements and be in the form (x y) where x and y are both integers, and return the area of the rectangle formed by the 4 points on a Cartesian grid. The 4 elements will be in arbitrary order. For example: if strArr is ["(0 0)", "(3 0)", "(0 2)", "(3 2)"] then your program should return 6 because the width of the rectangle is 3 and the height is 2 and the area of a rectangle is equal to the width * height. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.

def RectangleArea(strArr): 
  pts = [eval(p.replace(' ', ',')) for p in strArr]
  X = [x for x, y in pts]
  Y = [y for x, y in pts]
  return (max(X) - min(X)) * (max(Y) - min(Y))

# keep this function call here  
print RectangleArea(raw_input())