# Have the function CountingMinutesI(str) take the str parameter being passed which will be two times (each properly formatted with a colon and am or pm) separated by a hyphen and return the total number of minutes between the two times. The time will be in a 12 hour clock format. For example: if str is 9:00am-10:00am then the output should be 60. If str is 1:00pm-11:00am the output should be 1320. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.

def to_minutes(s):
    t = [int(t) for t in s[:-2].split(':')]
    if s.endswith('pm'):
        t[0] += 12
    return t[0] * 60  + t[1]


def CountingMinutesI(s): 
    mins = [to_minutes(s) for s in  s.split('-')]
    res= mins[1] - mins[0]
    if res < 0:
        res = 60*24 + res
    return res
    
    # code goes here 

    
# keep this function call here  
print CountingMinutesI(raw_input())


# Another Solution :

# def CountingMinutesI(s): 
#   at = list(s.replace('p','').replace('m','').replace('a','').replace('-',':').split(':'))
#   begt = int(at[0])*60+int(at[1])
#   endt = int(at[2])*60+int(at[3])
#   if (s.count('p') == s.count('a')):
#     if (s.index('p') < s.index('a')):
#       begt = begt + 12*60
#     else:
#       endt = endt + 12*60
#   if (endt < begt):
#     endt = endt + 24*60
#   return endt - begt
    
    
# # keep this function call here  
# # to see how to enter arguments in Python scroll down
# print CountingMinutesI(raw_input())