# /bin/env python3
# Created by: Enoch O
# Created on: May 14, 2025
# This program shall calculate/find the volume of a cube by obtaining its side.


def calculate_volume(side_length):
    return side_length**3


# Main function to get user input and display results
def main():
    while True:
        side_length_str = input("Enter the length of your cube (cm): ") #getting length as str

        try:
            side_length = float(side_length_str) # Turning the string to a float

            if side_length > 0 and side_length <= 1000:
                volume = calculate_volume(side_length)
                print(
                    f"The volume of the cube with side length {side_length} cm is {volume} cubic cm."
                ) # The result of the codes calculations
                break  #  Exit the loop after  calculation
            else:
                print("Error: Side length must be a between 0 and 1000 cm!!!")  # Users input MUST be between 0 - 1000 cm

        except ValueError:
            print("Invalid input. Please enter a positive number between 0 and 1000.") # Users input MUST be between 0 - 1000 cm


# Run the program
if __name__ == "__main__":
    main()
