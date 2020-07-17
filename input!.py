import sys
def silly_age_joke():
	print('How old are you?')
	age = int(sys. stdin.readline())
	if age >= 10 and age <= 13:
		print('''What is 123456+678901+23456789*2345678/2345678-23456782345678?
A headache?''')
	else: print('Huh?')

print("Type 'silly_age_joke()'")
