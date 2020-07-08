'''
Binary Search

by Chandan Agrawal

'''
def search(lst, a): 
	low = 0
	high = len(lst) - 1
	mid = 0

	while low <= high: 

		mid = (high + low) // 2

		if lst[mid] < a: 
			low = mid + 1

		elif lst[mid] > a: 
			high = mid - 1

		else: 
			return mid 

	return -1


lst = []
print("How many numbers in the list : ")
n = int(input())
print("Enter the numbers of the list : ")
i = 0
for i in range (n) :
    x = int(input())
    lst.append(x)
a = int (input ("Enter the number to be searched in the list : "))


out = search(lst, a) 

if out != -1: 
	print("Your number is present at index", str(out)) 
else: 
	print("Your number is NOT in the list") 
