# ask user for age
age = int(input("enter your age :"))
# if less than 13, qualified for the kiddie discount
if age < 13:
    print("you are qualified for the kiddie discount")
# if age is 21, congratulate
elif age ==21:
    print("congrats on your 21st!")
# if age is more than 65 but less than 100, retired
elif age >= 65:
    print("Enjoy your retirement!")
# if age more than 40 but less than 65, they are over the hill
elif age >= 40:
    print("you are over the hill.")
# if more than 100, good for them
elif age > 100:
    print("sorry, you are dead.")
# cover everything else
else:
    print("Age is but a number")