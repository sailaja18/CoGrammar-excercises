age = int(input("enter your age :"))
if age < 13:
    print("you are qualified for the kiddie discount")
elif age ==21:
    print("congrats onyour 21st!")
elif age >= 65:
    print("Enjoy your retirement!")
elif age >= 40:
    print("you are over the hill.")
elif age > 100:
    print("sorry, you are dead.")
else:
    print("Age is but a number")