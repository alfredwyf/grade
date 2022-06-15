#get user input of a numerical grade
grade = input("enter your grade: ")

#cast to an int
grade = int(grade)

#test the range of the number and print the appropriate letter grade
if grade >= 90:
	print('you got grade A')
elif grade >= 80:
	print('you got grade B')
elif grade >= 70:
	print('you got grade C')
elif grade >= 60:
	print('you got grade D')
else:
	print('you got grade F')
