# Have the function CharlietheDog(strArr) read the array of strings stored in strArr which will be a 4x4 matrix of the characters 'C', 'H', 'F', 'O', where C represents Charlie the dog, H represents its home, F represents dog food, and O represents and empty space in the grid. Your goal is to figure out the least amount of moves required to get Charlie to grab each piece of food in the grid by moving up, down, left, or right, and then make it home right after. Charlie cannot move onto the home before all pieces of food have been collected. For example: if strArr is ["FOOF", "OCOO", "OOOH", "FOOO"], then this looks like the following grid: 

 

# For the input above, the least amount of steps where the dog can reach each piece of food, and then return home is 11 steps, so your program should return the number 11. The grid will always contain between 1 and 8 pieces of food. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.

import itertools
def FindFood(a):
    food = []
    for row in range(len(a)):
        for col in range(len(a[row])):
            if a[row][col] == 'F':
                food.append([row, col])
    return food

def FindHome(a):
    for row in range(len(a)):
        for col in range(len(a[row])):
            if a[row][col] == 'H':
                return [row, col]

def FindCharlie(a):
    for row in range(len(a)):
        for col in range(len(a[row])):
            if a[row][col] == 'C':
                return [row, col]

def CharlietheDog(a):
    moves, food, charlie, home = 100, FindFood(a), FindCharlie(a), FindHome(a)
    pattern = list(itertools.permutations(food, len(food)))
    for pat in pattern:
        pat = list(pat)
        pat.append(home)
        pat.insert(0, charlie)
        m = 0
        last = pat[-1]
        for i in pat[::-1]:
            firsts, lasts = max(last[0],i[0])-min(last[0],i[0]), max(last[1],i[1])-min(last[1],i[1])
            m += lasts+firsts
            last = i
        if m < moves and m != 0:
            moves = m
    return moves
print CharlietheDog(raw_input())