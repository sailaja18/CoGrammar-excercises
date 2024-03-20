# This is task 14 which calculates holiday cost taking the users choice of city,length of stay and car rentals

print("Welcome to City breaks !!!")

# creating a list of  dictionaries to allow user choice for city selection 

cities = [
    {
        "name": "Lisbon",
        "flight": 300,
        "hotel": 100,
        "car": 50,
    },
    {
        "name": "London",
        "flight": 400,
        "hotel": 150,
        "car": 70,
    },
    {
        "name": "Berlin",
        "flight": 350,
        "hotel": 120,
        "car": 60,
    },
]

# Using list comprehension to get the selected city and using the lower function to convert it into lowercase
city_names = [city["name"] for city in cities]

# Allowing the user iput for choosing the number of days for car rental and stay   

city_of_choice = input(f"Please select the city of your choice from {city_names}: ").lower()

num_nights = int(input("Enter number of nights : "))

rental_days = int(input("Enter number of days for car hire : "))

selected_city = [city for city in cities if city["name"].lower() == city_of_choice][0]

# Defining function to get the flight charges as per the city selected
def plane_cost():
    
    flight_cost = selected_city["flight"]
    print(f"The cost of flight to {selected_city['name']} is {flight_cost} pounds")
    return flight_cost

#defining hotel_cost function to calculate hotel cost using if else loop depending on the number of nights selected 
def hotel_cost():
   
    if num_nights <= 7:
       hotel_cost = num_nights * selected_city["hotel"]
       print(f"Total hotel cost for {num_nights} nights is {hotel_cost} pounds.")
    
    else:
        print("Please enter a valid number!!")  
    
    return hotel_cost         

# Defining car_rental function to calaculate the car hire depending on user choice and validating it

def car_rental():
    
    if rental_days <= 7:
        car_rental = rental_days * selected_city["car"]
        print(f"Total cost of car hire for {rental_days} days is {car_rental} pounds.")
    else:
        print("Enter a valid number!!")
    return car_rental

# Defining the holiday_cost function to sum up all the individual cost to give the total holiday cost

def holiday_cost(flight_cost, hotel_cost, car_hire):
    
    total_cost = flight_cost + hotel_cost  + car_hire
    print(f"The total holiday cost for the trip is {total_cost} pounds.")
    return total_cost

# Assigning the return value of each of the three function to a three different variables respectively and calling the holiday_cost function
flight_cost = plane_cost()
hotel_cost = hotel_cost()
car_hire = car_rental()
holiday_cost(flight_cost, hotel_cost, car_hire)


