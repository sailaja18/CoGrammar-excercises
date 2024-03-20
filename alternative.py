"""
First part of this task takes a string from the user
and makes each alternative character upper and lower
case
"""
string_value = input("Please enter a string: ")
# initialise an empty string to hold final string
upper_lower_string = ""

# iterate through the word, from 0 to word length
for num in range(len(string_value)):
    # if the number if divisible by 2, its even number
    if (num % 2 == 0):
        # lower the letter and concatenate
        upper_lower_string += string_value[num].lower()
    else:
        # alternatively, upper the letter and concatenate
        upper_lower_string += string_value[num].upper()
print(upper_lower_string)       

"""
Second part of this task takes a sentence from the user
and makes each alternative word lower and upper
case
"""

sentence = input("Please enter a sentence: ")
# split the words in the sentence into a list
words_list = sentence.split()
print(words_list)

# for each word's index,
for num in range (len(words_list)):
    # if its odd numbered word, make it upper
    if num % 2 != 0:
        words_list[num] = words_list[num].upper()
        num += 1
    else:
        # even numbered word to be lower
        words_list[num] = words_list[num].lower()

print(words_list)
# join them together and print
lower_upper_sentence = " ".join(words_list) 
print(lower_upper_sentence)  
     