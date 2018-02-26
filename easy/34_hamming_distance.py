# Have the function HammingDistance(strArr) take the array of strings stored in strArr, which will only contain two strings of equal length and return the Hamming distance between them. The Hamming distance is the number of positions where the corresponding characters are different. For example: if strArr is ["coder", "codec"] then your program should return 1. The string will always be of equal length and will only contain lowercase characters from the alphabet and numbers. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.

def HammingDistance(strArr): 

  # get each word
  word1 = strArr[0]
  word2 = strArr[1]
 
  # store the final count
  count = 0
  
  # loop through one of the words and check to see if
  # each character from both words matches up
  for i in xrange(0, len(word1)):
    if word1[i] != word2[i]:
      count += 1
      
  return count
    
print HammingDistance(raw_input())