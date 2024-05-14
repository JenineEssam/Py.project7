import random


def generate_random_number(start, end):
    """Generate a random number between start and end."""
    return random.randint(start, end)


# Main function
def main():
    print("Welcome to the Random Number Generator!")

    # Get user input for the range of numbers
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))

    # Generate a random number
    random_number = generate_random_number(start, end)

    # Display the random number
    print(f"A random number between {start} and {end} is: {random_number}")


if __name__ == "__main__":
    main()
