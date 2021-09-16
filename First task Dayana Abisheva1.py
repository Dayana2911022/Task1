from itertools import permutations  
def allPermutations(list1):
     permList = permutations(list1)
     for perm in list(permList):
         print(perm)
z = int(input("Enter the characters:"))
listInput = []
for i in range(z):
	listInput.append(str(input()))

allPermutations(listInput)