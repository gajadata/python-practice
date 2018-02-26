# Have the function StarRating(str) take the str parameter being passed which will be an average rating between 0.00 and 5.00, and convert this rating into a list of 5 image names to be displayed in a user interface to represent the rating as a list of stars and half stars. Ratings should be rounded up to the nearest half. There are 3 image file names available: "full.jpg", "half.jpg", "empty.jpg". The output will be the name of the 5 images (without the extension), from left to right, separated by spaces. For example: if str is "2.36" then this should be displayed by the following image: 

 

# So your program should return the string "full full half empty empty". 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


import math
def StarRating(s):
    ns = []
    n = float(s)
    if n - math.floor(n) < (math.ceil(n) - 0.5) - n:
        n = math.floor(n)
    elif n - math.floor(n) < (math.ceil(n) - 0.5) - n:
        n = math.ceil(n) - 0.5
    while n > 0.5:
        ns.append("full")
        n -= 1
    while n > 0:
        ns.append("half")
        n -= 0.5
    while len(ns) < 5:
        ns.append("empty")
    return ' '.join(ns)
print StarRating(raw_input())