# This is task 14 which calculates holiday cost taking the users choice of city,length of stay and car rentals

# creating dictionary representing data for all cities
cities = {
    "Lisbon": {
        "flight": 300,
        "hotel": 100,
        "car": 50,
    },
    "London": {
        "flight": 400,
        "hotel": 150,
        "car": 70,
    },
    "Berlin": {
        "flight": 350,
        "hotel": 120,
        "car": 60,
    },
}

def hotel_cost(num_nights):
    """_summary_
    This function calculates total hotel cost given number of nights
    Note: Selected City is in the global variable,
        so as to keep the function definition as stated in the instructions
    Args:
        num_nights (int): Number of nights

    Returns:
        int: Total hotel cost, which is hotel cost for the city * number of nights
    """
    total_hotel_cost = num_nights * selected_city["hotel"]
    return total_hotel_cost

def plane_cost(city_flight):
    """_summary_
    This function calculates total plane cost given choice of city
    
    Args:
        city_flight (str): choice of city

    Returns:
        int: total plane cost
    """
    # Defining function to get the flight charges as per the city selected
    cost = city_flight["flight"]
    return cost

def car_rental(rental_days):
    """_summary_
    This function calculates total car rental cost given number of rental days
   
    Args:
        rental_days (int): number of days required 

    Returns:
        int: total_car_rental
    """
    total_car_rental = rental_days * selected_city["car"]
    return total_car_rental

def holiday_cost(hotel_cost, plane_cost, car_rental):
    total_cost = plane_cost + hotel_cost  + car_rental
    return total_cost


print("Welcome to City breaks !!!")

# Keep asking the user to select a valid city from the choices
while True:
    city_of_choice = input(f"Please select the city of your choice from {cities.keys()}: ").title()
    try:
        selected_city = cities[city_of_choice]
        break
    except KeyError:
        print("Please select a valid city from the choices, try again.")

# Once we have a valid city, ask the user for number of nights and rental days
num_nights = int(input("Enter number of nights : "))
rental_days = int(input("Enter number of days for car hire : "))

# Assigning the return value of each of the three functions to three different variables
# and calling the holiday_cost function with respective arguments
total_flight_cost = plane_cost(selected_city)
print(f"Flight cost for {city_of_choice} is £{total_flight_cost}.")
total_hotel_cost = hotel_cost(num_nights)
print(f"Total hotel cost for {num_nights} nights is £{total_hotel_cost}.")
total_car_hire = car_rental(rental_days)
print(f"Total cost of car hire for {rental_days} days is £{total_car_hire}.")
total_holiday_cost = holiday_cost(total_flight_cost, total_hotel_cost, total_car_hire)

print(f"Your total holiday cost will be: £{total_holiday_cost}.")
