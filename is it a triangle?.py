print('''Is it a triangle?
''')
print("Give the lengths of three sides:  ")
one = input("Side 1:  ")
error = one.isdecimal()
while error == False:
    print('''Please Give a Valid Number(positive, no letters, no special characters, whole etc.)''')
    one = input("Side 1:  ")
    error = one.isdecimal()
two = input("Side 2:  ")
error = two.isdecimal()
while error == False:
    print('''Please Give a Valid Number(positive, no letters, no special characters, whole etc.)''')
    two = input("Side 2:  ")
    error = two.isdecimal()
three = input("Side 3:  ")
error = three.isdecimal()
while error == False:
    print('''Please Give a Valid Number(positive, no letters, no special characters, whole etc.)''')
    one = input("Side 3:  ")
    error = three.isdecimal()
one = int(one)
two = int(two)
three = int(three)
if (one+two)>three and (one+three)>two and (two+three)>one:
    if (one**2+two**2) == three**2 or (two**2+three**2) == one**2 or (one**2 +three**2) == two**2:
        angle = 'right'
    elif (one**2+two**2) > three**2 or (two**2+three**2) > one**2 or (one**2 +three**2) > two**2:
        angle = 'acute'
    elif (one**2+two**2) < three**2 or (two**2+three**2) < one**2 or (one**2 +three**2) < two**2:
        angle = 'obtuse'
    if one != two and one != three and two != three:
        kind = 'scalene'
    elif one == two and one == three and two == three:
        kind = 'equilateral'
    elif one == two or one == three or two == three:
        kind = 'isosceles'
    print("Your values make up a", angle, ",", kind, "triangle.")
else:
    print("Your values do not make up a triangle.")
