
def celsius_to_fahrenheit(celsius):
  return (celsius * 9/5) + 32

def calculate_wind_chill(temp_fahrenheit, wind_speed_mph):
    wind_chill = (35.74 + (0.6215 * temp_fahrenheit)
                  - 35.75 * (wind_speed_mph ** 0.16)
                  + 0.4275 * temp_fahrenheit * (wind_speed_mph ** 0.16))
    return wind_chill

def main():
    # Get valid temperature input if they enter invalid input
    while True:
        try:
            temperature = float(input("What is the temperature? "))
            break
        except ValueError:
            print("Invalid temperature. Please enter a number.")

    # we want to be sure the user enters a valid unit
    while True:
        unit = input("Fahrenheit or Celsius (F/C)? ").strip().upper()
        if unit in ["F", "C"]:
            break
        else:
            print("Invalid unit. Please enter 'F' or 'C'.")

    # Convert to Fahrenheit if the user entered Celsius
    if unit == "C":
        temperature = celsius_to_fahrenheit(temperature)

    # loop true the program for wind chill calculation
    for wind_speed in range(5, 65, 5):
        wind_chill = calculate_wind_chill(temperature, wind_speed)
        print(f"At temperature {temperature:.1f}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}F")


# Run the program if __name__ == "__main__":
if __name__ == "__main__":
    print("Welcome to the Wind Chill Calculator!")
    print("This program calculates the wind chill based on temperature and wind speed.")
    print("You can enter the temperature in Fahrenheit or Celsius.")
    print("The wind speed will be calculated in increments of 5 mph from 5 to 60 mph.")
main()