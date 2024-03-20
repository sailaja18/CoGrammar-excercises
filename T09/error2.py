
# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion"  # Compilation error :Missing quotes as its a string 
animal_type = "cub"
number_of_teeth = 16
 # Logical error with full_spec : Missing the f-string to get the required output and usage of variables mixed up
full_spec = (f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth")  

print (full_spec) # Syntax Error : Missing paranthesis 
