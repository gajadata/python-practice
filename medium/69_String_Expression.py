# Have the function StringExpression(str) read the str parameter being passed which will contain the written out version of the numbers 0-9 and the words "minus" or "plus" and convert the expression into an actual final number written out as well. For example: if str is "foursixminustwotwoplusonezero" then this converts to "46 - 22 + 10" which evaluates to 34 and your program should return the final string threefour. If your final answer is negative it should include the word "negative." 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
ops = [('plus', '+'), ('minus', '-')]

def StringExpression(s):
    for x in ops:
        s = s.replace(x[0], x[1])
    for i in range(len(numbers)):
        s = s.replace(numbers[i], str(i))
    num = str(eval(s))
    res = ''
    for i in num:
        if i == '-':
            res += 'negative'
        else:
            res += numbers[int(i)]
    return res

# keep this function call here  
print StringExpression(raw_input())