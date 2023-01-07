import string

def askAgeAndCheck():
	while True:
		print('Enter your age:')
		age = input()
		try:
			age = int(age)
		except:
			print('Please use numeric digits.')
			continue
		if age < 1:
			print('Please enter a positive number.')
			continue
		break
	print(f'Your age is {age}.')
	return age
	


def doBandCheck():
	while True:
		print('Enter your date of birth:')
		dOB = input("dd/mm/yyyy:\n")
		print(type(dOB))
		dd, mm, yy = dOB.strip().split("/")

		dd = int(dd)
		mm = int(mm)
		yy = int(yy)

		print(dd, mm,yy)
		try:
			if int(dd) & dd <= 31 & dd > 0:
				if int(mm) & mm <= 12 & dd > 0:
					if int(yy) & yy <= 2019 & yy > 1900:
						continue
		except:
			print('Please use only numeric digits and respect the format.')
			continue

		break
	print(f'Your date of birth is {dd, mm, yy}.')

	return dd,mm,yy
	

def firstAndLastName():
	while True:
		print('Enter your first name:')
		firstName = input()
		if firstName.isalpha():
			break
		else:
			print('Please use letters only.')
			continue

	while True: 
		print('Enter your last name:')
		lastName = input()
		if lastName.isalpha():
			break
		else:
			print('Please use letters only.')
			continue

	print(f'Your name is {firstName} {lastName}.')
	return firstName,lastName
	



if __name__ == "__main__":

	age = askAgeAndCheck()
	fName, lName = firstAndLastName()
	day, month, year = doBandCheck()

