# Have the function Superincreasing(arr) take the array of numbers stored in arr and determine if the array forms a superincreasing sequence where each element in the array is greater than the sum of all previous elements. The array will only consist of positive integers. For example: if arr is [1, 3, 6, 13, 54] then your program should return the string "true" because it forms a superincreasing sequence. If a superincreasing sequence isn't formed, then your program should return the string "false" 

# Use the Parameter Testing feature in the box below to test your code with different arguments.

def Superincreasing(arr): 
    x = [int(c) for c in arr]
    sumnum = 0 
    counts = 0
    for i in range(0,len(x)-1):
        sumnum += x[i]
        if x[i+1] > sumnum:
            counts += 1
        else:
            return 'false'
    return 'true'
        

print Superincreasing(raw_input())


# Another Soluton :

# def Superincreasing(arr): 
#     s = arr[0]
#     for x in arr[1:]:
#         if x <= s:
#             return "false"
#         s += x
#     return "true"
    
# # keep this function call here  
# print Superincreasing(raw_input())