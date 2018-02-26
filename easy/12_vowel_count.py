#  Using the Python language, have the function VowelCount(str) take the str string parameter being passed and return
# the number of vowels the string contains (ie. "All cows eat grass" would return 5). Do not count y as a vowel for
# this challenge.


def VowelCount(a_string):
	idx = 0
	for i in a_string:
		if i in ['a','e','i','o','u']:
			idx += 1

	print ('Vowel Count : %d ' % idx )


VowelCount(raw_input())



