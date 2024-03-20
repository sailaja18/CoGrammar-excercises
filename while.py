total = 0
count = 0
user_number = int(input("Please eneter a number :"))

while user_number != -1:
    total = total+user_number
    count += 1
    user_number = int(input("Please eneter a number :"))
    average = total/count
print(total)
print(count)
print("Average of the numbers is :" ,average)

