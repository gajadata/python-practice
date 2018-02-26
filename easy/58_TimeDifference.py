# Have the function TimeDifference(strArr) read the array of strings stored in strArr which will be an unsorted list of times in a twelve-hour format like so: HH:MM(am/pm). Your goal is to determine the smallest difference in minutes between two of the times in the list. For example: if strArr is ["2:10pm", "1:30pm", "10:30am", "4:42pm"] then your program should return 40 because the smallest difference is between 1:30pm and 2:10pm with a difference of 40 minutes. The input array will always contain at least two elements and all of the elements will be in the correct format and unique. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.




def GetMinutes(time):
    h,m = map(int, time[:-2].split(':'))
    tag = time[-2:]
    if h == 12 and tag.lower() == 'am':
        h = 0
    elif h != 12 and tag.lower() == 'pm':
        h += 12
    return h * 60 + m

def TimeDifference(strArr): 
    times = sorted(map(GetMinutes, strArr))
    smallest = 24 * 60 + times[0] - times[-1]
    for i in range(1, len(times)):
        smallest = min(smallest, times[i] - times[i-1])
    return smallest
    
# keep this function call here  
print TimeDifference(raw_input())