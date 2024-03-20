import math #  importing math function to calculate  
choice = str(input("please enter your choice either investment or bond to proceed: "))  #user inputs to choose
choice = choice.lower()  # converting the user input to lower case
print(choice)  # printing users choice
if (choice != "investment") and (choice != "bond"):  # checking if user input deoesn't match the options given
    print("please enter a valid choice!!!")  #generating an error message if the input doesnt match the criteria

if choice == "investment":  #if the user inputs investment then asking the use to input more information  

    deposit_amount = int(input("please enter the amount of money to deposit:"))
    interest_rate = int(input("please enter the interest rate:"))
    number_of_years = int(input("please enter the number of years to invest:"))
    interest = input("please enter if its simple or compound interest:")  # asking the user to choose his option for interest
    
    if interest == "simple":  #if the user chooses simple interest calculating the required
        total_amount = deposit_amount * (1+(interest_rate/100) * number_of_years)
        print("The total amount when simple interest is applied is:",total_amount)

    elif interest == "compound":  #depending on the choice calculating as required
        total_amount = deposit_amount * math.pow((1+(interest_rate/100)),number_of_years)
        print("The total amount when compound interest is applied is:",total_amount)

else :  #if the user chooses bond requesting the related information needed

    present_value = int(input("enter the present value of the house:")) #requesting more information
    interest_rate = int(input("please enter the interest rate :"))
    number_of_months = int(input("number of months planned to repay :")) 

    interest_monthly = (interest_rate/100)/12
    print(interest_monthly)
    repayment = (interest_monthly * present_value)/(1 - (1 + interest_monthly)**(-number_of_months))  #calculating the monthly payment

    print("the monthly repayment is",repayment)  #displaying the monthly payment as output

   

