# Have the function KUniqueCharacters(str) take the str parameter being passed and find the longest substring that contains k unique characters, where k will be the first character from the string. The substring will start from the second position in the string because the first character will be the integer k. For example: if str is "2aabbacbaa" there are several substrings that all contain 2 unique characters, namely: ["aabba", "ac", "cb", "ba"], but your program should return "aabba" because it is the longest substring. If there are multiple longest substrings, then return the first substring encountered with the longest length. k will range from 1 to 6. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def KUniqueCharacters(s):
    k = int(s[0])
    subs = ''
    for i in xrange(1, len(s)):
        unique = set()
        new_subs = ''
        for x in s[i:]:
            unique.add(x)
            if len(unique) > k:
                break
            new_subs += x
        if len(new_subs) > len(subs):
            subs = new_subs
    return subs

# keep this function call here
print KUniqueCharacters(raw_input())