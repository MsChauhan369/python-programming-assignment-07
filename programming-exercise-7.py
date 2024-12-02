def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    # Step 1: Gather user information
    name = input("Hello! What's your name? ")
    print(f"Nice to meet you, {name}!")
    
    # Step 2: Store numbers in a list
    numbers = []
    for i in range(3):
        num = int(input(f"Please enter your favorite number #{i + 1}: "))
        numbers.append(num)

    # Step 3: Check even or odd
    even_odd_list = [(num, "even" if num % 2 == 0 else "odd") for num in numbers]

    # Step 4: Create tuples of numbers and their squares
    squares_list = [(num, num ** 2) for num in numbers]

    # Step 5: Calculate the sum of the numbers
    total_sum = sum(numbers)
    print(f"\nThe sum of your favorite numbers is: {total_sum}. Keep it up, {name}!")

    # Step 6: Check if the sum is prime
    if is_prime(total_sum):
        print(f"Genius, {total_sum} is a prime number! That's awesome!")
    else:
        print(f"Try again! {total_sum} is not prime number, but you can try if you want") 

    # Display even/odd and squares
    print("\nHere's a fun summary of your numbers:")
    for num, status in even_odd_list:
        print(f"Number: {num} is {status}.")
    
    print("\nAnd here are your numbers with their squares:")
    for num, square in squares_list:
        print(f"{num} squared is {square}.")

if __name__ == "__main__":
    main()
