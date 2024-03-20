# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

#print "Welcome to the error program"--->syntax error : missing brackets
print ("Welcome to the error program")
#print "\n"-->syntax error : indentation and missing brackets
print ("\n")

# Variables declaring the user's age, casting the str to an int, and printing the result
# age_Str == "24 years old" #-->syntax error : indentation and use of logical operator for equal to
# ValueError: invalid literal for int() with base 10: '24 years old'
age_Str = "24"

#age = int(age_Str)#--> syntax error : indentation
age = int(age_Str)

#print("I'm" + age + "years old.")#--> syntax error : indentation and use of wrong variable for concatinating 
print("I'm " + age_Str + " years old.")

# Variables declaring additional years and printing the total years of age
   
# years_from_now = "3" #--> syntax error : indentation
years_from_now = "3"

#total_years = age + years_from_now #--> syntax error : indentation
total_years = age + int(years_from_now)

#print "The total number of years:" + "answer_years"-->syntax error : missing brackets and use of wrong variable 
                                                      # answer_years instead of total_years
print("The total number of years:" ,total_years)

# Variable to calculate the total amount of months from the total amount of years and printing the result

#total_months = total * 12---.undefined variable total instaed of total_years and logical error as per the desired output
total_months = total_years * 12
final_total = total_months + 6

#print "In 3 years and 6 months, I'll be " + total_months + " months old"-->syntax error : missing bracket and 
# casting total_months to string
print ("In 3 years and 6 months, I'll be " + str(final_total) + " months old")


#HINT, 330 months is the correct answer 