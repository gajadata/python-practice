# Have the function CommandLine(str) take the str parameter being passed which represents the parameters given to a command in an old PDP system. The parameters are alphanumeric tokens (without spaces) followed by an equal sign and by their corresponding value. Multiple parameters/value pairs can be placed on the command line with a single space between each pair. Parameter tokens and values cannot contain equal signs but values can contain spaces. The purpose of the function is to isolate the parameters and values to return a list of parameter and value lengths. It must provide its result in the same format and in the same order by replacing each entry (tokens and values) by its corresponding length. 

# For example, if str is: "SampleNumber=3234 provider=Dr. M. Welby patient=John Smith priority=High" then your function should return the string "12=4 8=12 7=10 8=4" because "SampleNumber" is a 12 character token with a 4 character value ("3234") followed by "provider" which is an 8 character token followed by a 12 character value ("Dr. M. Welby"), etc. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def CommandLine(s):
    s = s
    arr = []
    word = ""
    result = ""
    for x in s:
        if x == "=":
            if word.count(" ")==0:
                arr.append(word)
            else:
                y = word.rfind(" ")
                arr.append(word[0:y])
                arr.append(word[y+1:])
            word = ""
        else:
            word += x
    arr.append(word)
    count = 2
    #print arr
    for x in arr:
        if count%2 == 0:
            result += str(len(x))
        else:
            result += "="+str(len(x))+ " "
        count += 1
    return result
print CommandLine(raw_input())