def trip_welcome(origin, destination):
    print("Welcome to Tripcademy!")
    print("Looks like you are traveling from " + origin + " to " + destination)
    print("Let's get you to your destination.")


def directions_to_timesSq():
    print("Walk 4 mins to 34th St Herald Square train station")
    print("Take the Northbound N, Q, R, or W train 1 stop")
    print("Get off the Times Square 42nd Street stop")
    print("Take lots of pictures!")


def weather_check():
    print("It's raining outside. Bring an umbrella!")


def generate_trip_instructions(location):
    print("Looks like you are planning a trip to visit " + location)
    print("You can use the public subway system to get to " + location)


def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
    car_rental_total = car_rental_rate * trip_time
    hotel_total = hotel_rate * trip_time - 10

    trip_total = car_rental_total + hotel_total + plane_ticket_price
    return trip_total

def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0 " + name)

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

def destination_setup(origin, destination, estimated_time, mode_of_transport = "Car"):
  print("Your trip starts off in " + origin)
  print("And you are traveling to " + destination)
  print("You will be traveling by " + mode_of_transport)
  print("It will take approximately " + str(estimated_time) + " hours")

# Step 5: call your function
print(calculate_expenses(200, 100, 100, 5))

trip_planner_welcome("Johnny")
estimate = estimated_time_rounded(14.5)
destination_setup("Paris", "Rome", estimate, "train")

# generate_trip_instructions("Central Park")
# generate_trip_instructions("Grand Central Station")

# directions_to_timesSq()
