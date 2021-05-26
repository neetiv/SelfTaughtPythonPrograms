def integer_numbers():
    inp = input("Give three numbers(seperated by commas):  ")
    nums = inp.split(',')
    #print(nums)
    one = []
    two = []
    three = []

    def factors(x,y):
        for g in range(1,(x)+1):
            if int(x) % g == 0:
                y.append(g)
        
        print("The factors of",x,"are: ",y)

    nums[0]=int(nums[0])
    nums[1]=int(nums[1])
    nums[2]=int(nums[2])

    factors(nums[0],one)
    factors(nums[1],two)
    factors(nums[2],three)


    gcd = 1
    for i in range(0, len(one)):
        for j in range(0, len(two)):
            for t in range(0, len(three)):
                if one[-1*i] == two[-1*j] and one[-1*i] == three[-1*t] and three[-1*t] == two[-1*j]:
                    gcd=(one[-1*i])
                    break
            if gcd>1:
                break
        if gcd>1:
            break
    print(gcd, "is the GCD of", nums[0], ",", nums[1], "and", nums[2])


    multiple=1
    while True:
        if multiple%nums[0] == 0 and multiple%nums[1]==0 and multiple%nums[2]==0:
            lcm=multiple
            break
        else:
            multiple=multiple+1
        
    print("The LCM of",nums[0],",",nums[1],"and", nums[2], "is",lcm)

            
    if gcd == 1:
        print(nums[0], ",", nums[1], "and", nums[2], "are relatively prime.")


from tkinter import *
integer = Tk()
button = Button(integer, text="start program", command=integer_numbers)
