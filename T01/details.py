#Pseudo Code:
#request input name from user 
#store the input in variable user_name
#request second input age from the user
#store this second input in variable user_age 
#request third input house number from the user
#store this thirdi nput in variable house_number 
#request fourth input street name from the user
#store this fouth input in variable street_name
#using f-string create a string using all the input given in the format given and assign it to variable to_print
#print to_print




user_name = input("enter your name : ")
user_age = input("enter your age : ")
house_number = input("enter house number : ")
street_name = input("enter street name : ") 
to_print = f"this is {user_name} who is {user_age} years old and lives at {house_number} on {street_name}."
#print("This is  " +  user_name + "." + " He is "  + user_age + "years old and lives at " + house_number + " on " + street_name + "." )
print(to_print)