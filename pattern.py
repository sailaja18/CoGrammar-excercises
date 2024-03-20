#This can be done in two ways 1) Using if-else inside a for loop and 2) Using for loop on its own
# The first code is using for loop using if-else and is commented to stop its execution.
"""pattern = "@"
for i in range(1,10):
    if i <= 6:
        num_value = pattern *i
        print(num_value)
    else:
       count_down = 10-i
       num_value = count_down * pattern
       print(num_value)
    """
    
    
pattern = "*"  # declaring a variable and assigning it value to print for the pattern
for i in range (1,10): #using for loop to make 9 iterations
    to_print = i*pattern # using logic to achieve the output and assigining it to a variable
    if i >=6: #using if condition to check the iterating value and carry on the code assigned under 
        count_down = 10-i  # using logic to decrease the count value and assigning it to a variable
        to_print = count_down * pattern # using the countdown and logic to get the needed pattern
    print(to_print)   # printing the variable value after applyoing the logic    

    
