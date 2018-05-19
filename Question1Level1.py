## Question
## Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
## between 2000 and 3200 (both included).
## The numbers obtained should be printed in a comma-separated sequence on a single line.

## Hints: 
## Consider use range(#begin, #end) method


## Function
## Param: None
## Input: None
## Output: None
## Return: a list of numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included)

def getNumList():
	# Initialize a number list
	numList = []
	
	for num in range(2000, 3201):
		if num%7 == 0:
			if num%5 != 0:
				numList.append(num)
	
	return numList



def main():
	numList = getNumList()

	numString = ''
	for i in range(0, len(numList)-1):
		
		numString = numString + str(numList[i]) + ', '
	
	numString = numString + str(numList[-1])
		
	print(numString)


main()
	