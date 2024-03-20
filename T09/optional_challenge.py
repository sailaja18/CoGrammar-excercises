pattern = "@"
for i in range(1,10):
    if i < 6 # Compilation error : misssing indentataion
             # logical error : The output is not as desired to to error in the logic it shouldn't be equal to 6 as well 
        num_value = pattern *i
        print(num_value)
    else:
       count_down = 10-i
       num_value = count * pattern # runtime eror : count unkown
       print num_value) # compilation error : missing brackets