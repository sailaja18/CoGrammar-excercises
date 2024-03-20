
string_value = input("Please enter a string : ")
string_value_new = " "

for num in range(len(string_value)):
    if (num % 2 == 0):
        string_value_new += string_value[num].lower()
    else:
        string_value_new += string_value[num].upper()
print(string_value_new)       
           
string_value = input("Please enter a string : ") 
string_value_1 = string_value.split()    

print(string_value_1)

for num in range (len(string_value_1)):
    if num % 2 != 0:
        string_value_1[num] = string_value_1[num].upper()
        num += 1
    else:
        string_value_1[num] = string_value_1[num].lower()

print(string_value_1)
string_value_1 = " ".join(string_value_1) 
print(string_value_1)  
     