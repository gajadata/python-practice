# Have the function DashInsert(str) insert dashes ('-') between each two odd numbers in str. For example: if str is 454793 the output should be 4547-9-3. Don't count zero as an odd number. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.

def DashInsert(s): 

	l = list(s)

	for i in range(0,len(l)-1):
		if (int(l[i]) % 2 != 0 and int(l[i+1]) % 2 != 0 ):
			l[i] = l[i] + '-'

	return ''.join(l)

    
# keep this function call here  
print DashInsert(raw_input())