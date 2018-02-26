# Have the function DivisionStringified(num1,num2) take both parameters being passed, 
# divide num1 by num2, and return the result as a string with properly formatted commas. 
# If an answer is only 3 digits long, return the number with no commas 
# (ie. 2 / 3 should output "1"). 
# For example: if num1 is 123456789 and num2 is 10000 the output should be "12,346". 
# 1 - One
# 10 - Ten
# 100 - One hundred
# 1,000 - One thousand
# 10,000 - Ten thousand
# 100,000 - One hundred thousand
# 1,000,000 - One million
# 10,000,000 - Ten million
# 100,000,000 - One hundred million
# 1,000,000,000 - One billion 



def DivisionStringified(num1, num2): 


  # first we convert the integers to floating point
  # then divide and round accordingly
  div = round(float(num1)/float(num2))

  # convert answer to integer then to a string and 
  # finally into a list separating each number
  div = list(str(int(div)))
  
  # keep counter for inserting comma logic
  insert = 0
  
  # logic for inserting a comma every 3 elements into the reversed list
  # we use the enumerate function along with the reversed function to
  # loop backwards through the list while maintaining list indices
  # e.g. ['4', '5', '3', '2'] becomes ['4', ',5', '3', '2']
  # and then we would join all the numbers into a string
  if len(div) > 3:
    for i, e in reversed(list(enumerate(div))):
      insert = insert + 1
      if (insert == 3):
        div[i] = ',' + e
        insert = 0
  
  # return the elements joined into a proper string
  return ''.join(div)
# keep this function call here  
num1,num2=map(int,raw_input().split())
print DivisionStringified(num1,num2)
	

# Another Solution :

# def DivisionStringified(num1,num2): 
#   answer = int(round(float(num1) / float(num2)))
#   s = ''
#   while answer != 0:
#     s = str(answer % 1000) + ',' + s
#     answer /= 1000
#   return s[:-1]
    
    
# # keep this function call here  
# # to see how to enter arguments in Python scroll down
# print DivisionStringified(raw_input())

# fastest Way :

# def DivisionStringified(num1,num2): 
#   return '{:,}'.format( (num1+(num2/2))/num2)
    
    
# # keep this function call here  
# # to see how to enter arguments in Python scroll down
# print DivisionStringified(raw_input())


