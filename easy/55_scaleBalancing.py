# Have the function ScaleBalancing(strArr) read strArr which will contain two elements, the first being the two positive integer weights on a balance scale (left and right sides) and the second element being a list of available weights as positive integers. Your goal is to determine if you can balance the scale by using the least amount of weights from the list, but using at most only 2 weights. For example: if strArr is ["[5, 9]", "[1, 2, 6, 7]"] then this means there is a balance scale with a weight of 5 on the left side and 9 on the right side. It is in fact possible to balance this scale by adding a 6 to the left side from the list of weights and adding a 2 to the right side. Both scales will now equal 11 and they are perfectly balanced. Your program should return a common separated string of the weights that were used from the list in ascending order, so for this example your program should return the string 2,6 

# There will only ever be one unique solution and the list of available weights will not be empty. It is also possible to add two weights to only one side of the scale to balance it. If it is not possible to balance the scale then your program should return the string not possible. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def ScaleBalancing(strArr):
    x,y = eval(strArr[0])
    w = eval(strArr[1])

    for i in range(0, len(w)):
        if x + w[i] == y or y + w[i] == x:
            return w[i]
        for j in range(i + 1, len(w)):
            if x + w[i] == y + w[j] or x + w[j] == y + w[i] or x + w[i] + w[j] == y or x == y + w[i] + w[j]:
                return str(w[i]) + ',' + str(w[j])
    # code goes here
    return 'not possible'

# keep this function call here
print ScaleBalancing(raw_input())