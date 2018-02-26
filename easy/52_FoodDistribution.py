# Have the function FoodDistribution(arr) read the array of numbers stored in arr which will represent the hunger level of different people ranging from 0 to 5 (0 meaning not hungry at all, 5 meaning very hungry). You will also have N sandwiches to give out which will range from 1 to 20. The format of the array will be [N, h1, h2, h3, ...] where N represents the number of sandwiches you have and the rest of the array will represent the hunger levels of different people. Your goal is to minimize the hunger difference between each pair of people in the array using the sandwiches you have available. 

# For example: if arr is [5, 3, 1, 2, 1], this means you have 5 sandwiches to give out. You can distribute them in the following order to the people: 2, 0, 1, 0. Giving these sandwiches to the people their hunger levels now become: [1, 1, 1, 1]. The difference between each pair of people is now 0, the total is also 0, so your program should return 0. Note: You may not have to give out all, or even any, of your sandwiches to produce a minimized difference. 

# Another example: if arr is [4, 5, 2, 3, 1, 0] then you can distribute the sandwiches in the following order: [3, 0, 1, 0, 0] which makes all the hunger levels the following: [2, 2, 2, 1, 0]. The differences between each pair of people is now: 0, 0, 1, 1 and so your program should return the final minimized difference of 2. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.

minval = 1<<30
def distnext(b):
    global minval
    m = b.pop(0)
    minval = min(minval, sum([abs(b[j+1]-b[j]) for j in range(len(b)-1)]))
    if m==0 or min(b) == max(b): return
    for i,x in enumerate(b):
        d1 = i>0 and abs(x-b[i-1]) + i<len(b)-1 and abs(x-b[i+1])
        d2 = i>0 and abs(x-1-b[i-1]) + i<len(b)-1 and abs(x-1-b[i+1])
        if x>0 and d2<=d1:
            distnext([m-1]+b[:i]+[x-1]+b[i+1:])
    return
    
def FoodDistribution(a): 
    distnext(a)
    return minval  
    
# keep this function call here  
print FoodDistribution(raw_input())