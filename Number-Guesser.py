import random

#Taking input from user to enter the top of the range from which the number will be generated. The lower bound of the range will be set to '0'.
top_of_Range = input("Type a number: ")

#Checking to see if the input given by user is a number or a string.
if top_of_Range.isdigit():
    top_of_Range = int(top_of_Range) #Coverting the input into 'int', because python by default converts the inputs to string. This will also convert the float number given by user to the nearest integer, which eliminates the possibilty of having the random number range in float or any other number type.
    if top_of_Range <=0:
        print("Please enter a number greater than zero next time.")
        quit()
else:
    print("Please enter a valid number.")
    quit()

#Randrange is a function which will generate a number within the range of '0' to '10'. Notice that I have put 11 in the upper bound range but it will only one generate the number lower from the given range. In this case the upper bound is 11 and the maximum number would be generated is 10.
#To include the given parameter as the upper bound, you can use the 'randint()' function. It will generate a random integer which includes both given parameters as the upper and lower bounds, respectively.
#If you only give one parameter to the function, then '0' will be considered as the lower bound and the given number will be considered as the upper bound. But also note that this approach will not work with negative numbers. For that you will have to add both parameters.
random_number =random.randrange(top_of_Range)
print(random_number)
