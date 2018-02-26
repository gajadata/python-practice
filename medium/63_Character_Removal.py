# Have the function CharacterRemoval(strArr) read the array of strings stored in strArr, which will contain 2 elements: the first element will be a sequence of characters representing a word, and the second element will be a long string of comma-separated words, in alphabetical order, that represents a dictionary of some arbitrary length. For example: strArr can be: ["worlcde", "apple,bat,cat,goodbye,hello,yellow,why,world"]. Your goal is to determine the minimum number of characters, if any, can be removed from the word so that it matches one of the words from the dictionary. In this case, your program should return 2 because once you remove the characters "c" and "e" you are left with "world" and that exists within the dictionary. If the word cannot be found no matter what characters are removed, return -1. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.



def CharacterRemoval(a):
    d, w, s = a[1].split(','), a[0], len(a[1])
    for i in d:
        c, flag = list(w[:]), True
        for letter in i:
            if letter in c:
                c.remove(letter)
            else:
                flag = False
        if flag:
            if len(c) < s:
                s = len(c)
    if s == len(a[1]):
        return -1
    else:
        return s
print CharacterRemoval(raw_input())