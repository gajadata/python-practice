# Have the function PairSearching(num) take the num parameter being passed and perform the following steps. First take all the single digits of the input number (which will always be a positive integer greater than 1) and add each of them into a list. Then take the input number and multiply it by any one of its own integers, then take this new number and append each of the digits onto the original list. Continue this process until an adjacent pair of the same number appears in the list. Your program should return the least number of multiplications it took to find an adjacent pair of duplicate numbers. 

# For example: if num is 134 then first append each of the integers into a list: [1, 3, 4]. Now if we take 134 and multiply it by 3 (which is one of its own integers), we get 402. Now if we append each of these new integers to the list, we get: [1, 3, 4, 4, 0, 2]. We found an adjacent pair of duplicate numbers, namely 4 and 4. So for this input your program should return 1 because it only took 1 multiplication to find this pair. 

# Another example: if num is 46 then we append these integers onto a list: [4, 6]. If we multiply 46 by 6, we get 276, and appending these integers onto the list we now have: [4, 6, 2, 7, 6]. Then if we take this new number, 276, and multiply it by 2 we get 552. Appending these integers onto the list we get: [4, 6, 2, 7, 6, 5, 5, 2]. Your program should therefore return 2 because it took 2 multiplications to find a pair of adjacent duplicate numbers (5 and 5 in this case). 

# Use the Parameter Testing feature in the box below to test your code with different arguments.

nmul = 1<<20
def pairnext(s, num, n):
    global nmul
    if n>nmul: return
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            nmul = min(nmul,n)
            return
    snum = str(num)
    for c in snum:
        if c=='1' and s[-1]!=snum[0] and snum[0]!=snum[-1]: continue
        if c=='0': 
            nmul = min(nmul, n+1)
            continue
        pairnext(s+str(num*int(c)), num*int(c), n+1)
    return
    
def PairSearching(num): 
    pairnext(str(num), num, 0)
    return nmul
    
# keep this function call here  
print PairSearching(raw_input())