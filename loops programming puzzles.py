print('Loops Programming Puzzles')
print('      ')
print('#1: The Hello Loop')
print('I think that nothing will happen when I run this code because the loop will break before x will ever reach 9')
print('   ')
for x in range(0,20):
    print('hello %s' % x)
    if x< 9:
        break


print('   ')
print('#2: Even Numbers')
value = 0
for x in range(0, 12):
    value = value + 2
    print(value)
    if value == 12:
        break


print('   ')
print('#3: My Five Favorite Pizza Toppings')
ingredients = ['olives', 'mushrooms', 'onions', 'tomaetoes', 'peppers']
for ingredient_number in range(1, 6):
    print(ingredient_number, ingredients[ingredient_number-1])


