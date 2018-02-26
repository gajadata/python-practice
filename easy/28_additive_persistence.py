def AdditivePersistence(num): 
  return 0 if num <10 else 1 + AdditivePersistence(sum([int(c) for c in str(num)]))
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print AdditivePersistence(raw_input())