print('''Functions: Programming Puzzles

''')

print('''#1: Mystery Code
''')
print(''' I think that when the code prints 'a' it will print the number 20, and when it prints 'b' it will print the number 0''')

print('''code test:
''')

a = abs(10)+abs(-10)
print(a)
b = abs(-10)+-10
print(b)


print('''
#2: Copying a File
''')

test_file = open('/Users/neeti/test.txt')
print(test_file.read())

test_file = open('c:\\copy.txt', 'w')
test_file.write('''HELLOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
Hekfjdk
‘vnkdp[v
Dvd
]slkb


YES< this makes total sense.''')

test_file.close()

test_file = open('copy.txt')
print(test_file.read)
