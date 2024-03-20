swimming = int(input("enter the time taken for swimming:"))
cycling = int(input("enter the time taken for cycling:"))
running = int(input("enter the time taken for running:"))
total_time = swimming+cycling+running
print(total_time)
qualifying_time = total_time
if qualifying_time <= 100:
    print("you received provincial bond award")
elif qualifying_time <= 105:
    print("you received Provincial Half colours award")
elif qualifying_time <= 110 :
    print("you received Provincial Scroll")
else:
    print("you didn't receive any award")
