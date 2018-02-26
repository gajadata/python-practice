# Have the function NumberSearch(str) take the str parameter, search for all the numbers in the string, add them together, then return that final number. For example: if str is "88Hello 3World!" the output should be 91. You will have to differentiate between single digit numbers and multiple digit numbers like in the example above. So "55Hello" and "5Hello 5" should return two different answers. Each string will contain at least one letter or symbol. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.

def NumberAddition(s): 
	num = 0
	res = 0
	for c in s:
		if c.isdigit():
			num = num * 10 + int(c)
		else:
			res += num
			num = 0
	res += num
	return res

# keep this function call here  
print NumberAddition(raw_input())


# Another Solution :

# def NumberAddition(s): 
#   num = 0
#   res = 0
#   for c in s:
#     if c.isdigit():
#        num = num * 10 + int(c)
#     else:
#        res += num
#        num = 0
#   res += num
#   return res
    
# # keep this function call here  
# # to see how to enter arguments in Python scroll down
# print NumberAddition(raw_input())