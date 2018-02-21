#  Using the Python language, have the function ABCheck(str) take the str parameter being passed and return the string
# true if the characters a and b are separated by exactly 3 places anywhere in the string at least once (ie.
# "lane borrowed" would result in true because there is exactly three characters between a and b). Otherwise
# return the string false.

# def ABCheck(a_string):

#     for index in xrange(len(a_string) - 4):
#         if a_string[index] == 'a':
#             if a_string[index + 4] == 'b':
#                 return True
#         elif a_string[index] == 'b':
#             if a_string[index + 4] == 'a':
#                 return True
#     return False


def ABcheck(a_string):
	a_idx = ''
	b_idx = ''
	for i,idx in enumerate(a_string.lower()):
		if idx in ('a'):
			a_idx = i
			#b_idx = i
			print a_idx
			print b_idx

		if idx in ('b'):
			#a_idx = i
			b_idx = i
			print a_idx
			print b_idx

		if a_idx and b_idx != '' :
			break
			print a_idx,b_idx

	if abs(int(a_idx) - int(b_idx)) == 4:
		print True
	else :
		print False

ABcheck(raw_input())




