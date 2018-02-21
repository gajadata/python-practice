# Have the function AlphabetSoup(str) take the str string parameter being passed and return the string with the letters
# in alphabetical order (ie. hello becomes ehllo). Assume numbers and punctuation symbols will not be included in the string.

# def AlphabetSoup(a_string):
#     list_of_chars = []

#     for char in a_string.lower():
#         list_of_chars.append(char)

#     ordered_list = sorted(list_of_chars)
#     alphabetical_string = ''.join(ordered_list)

#     return alphabetical_string


def AlphabetSoup(a_string):
	reverse_string = ''
	b_string = sorted(a_string)
	for i in b_string:
		reverse_string += i

	print (reverse_string)

AlphabetSoup(raw_input())


