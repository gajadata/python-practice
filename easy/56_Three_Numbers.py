# Have the function ThreeNumbers(str) take the str parameter being passed and determine if exactly three unique, single-digit integers occur within each word in the string. The integers can appear anywhere in the word, but they cannot be all adjacent to each other. If every word contains exactly 3 unique integers somewhere within it, then return the string true, otherwise return the string false. For example: if str is "2hell6o3 wor6l7d2" then your program should return "true" but if the string is "hell268o w6or2l4d" then your program should return "false" because all the integers are adjacent to each other in the first word. Use the Parameter Testing feature in the box below to test your code with different arguments.

def ThreeNumbers(s):
    for w in s.split():
        trw = [ch for ch in w if ch.isdigit()]
        if len(trw) != 3 or len(trw) != len(set(trw)) or w.find(''.join(trw)) != -1:
            return "false"
    return "true"

# keep this function call here
print ThreeNumbers(raw_input())