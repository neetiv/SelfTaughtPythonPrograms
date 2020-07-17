print('Moon Weight Calculator')
print('''

''')
import sys
def moon_weight():
    print('Please enter your current Earth weight')
    weight = int(sys.stdin.readline())
    print('Please enter the amount in kilos your weight might increase each year, rounded to the nearest whole number')
    increase = int(sys.stdin.readline())
    print('Please enter the number of years you will be on the moon')
    years = int(sys.stdin.readline())
    moon_weight = (weight*0.165) + (increase*years)
    print('Your weight after being on the moon for %s years is %s' % (years, moon_weight))
moon_weight()
