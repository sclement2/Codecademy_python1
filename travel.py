def trip_welcome():
    print("Welcome to Tripcademy!")
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


generate_trip_instructions("Central Park")
generate_trip_instructions("Grand Central Station")

# directions_to_timesSq()
