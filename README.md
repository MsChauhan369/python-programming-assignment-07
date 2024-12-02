
# Contents of Table

[1- Assignment-title](#python-programming-assignment-07)

[2- This is function to cover the stpes](#this-is-function-to-cover-the-steps)

[2.1- Gather User Information](#step-1--gather-user-information)

[3- Store Numbers in a List](#step-2-store-numbers-in-a-list)

[4- check-even-or-odd](#step-3-check-even-or-odd)

[5- Create Tuples of Numbers and Their Squares](#step-4-create-tuples-of-numbers-and-their-squares)

[6- Calculate the Sum of the Numbers](#step-5-calculate-the-sum-of-the-numbers)

[7- Check if the Sum is Prime](#step-6-check-if-the-sum-is-prime)

[8- Display even/odd and squares](#7-display-evenodd-and-squares)

[9- complete code available on just one click](#8-complete-code-available-on-just-one-click)

[10- Ref by Jahanzaib Tayyab Github-portal](#9-jahanzaib-tayyab-github-portal)

# Python Programming Assignment 07:

## You are tasked with creating a Python program that serves as an interactive tool for a friend who enjoys exploring numbers. The program should begin by prompting the user to enter their name and then ask them for three of their favorite numbers. After gathering this information, the program should greet the user with a personalized message that includes their name. The three numbers provided by the user should be stored in a list. The program should then check if any of the numbers are even or odd, and store this information in a separate list of tuples, where each tuple contains the number and a string indicating whether it is "even" or "odd". Following this, the program should use a for loop to iterate over the list of numbers, and for each number, it should create a tuple containing the number and its square. These tuples should be printed in a creative and engaging format. Additionally, the program should calculate the sum of the three numbers and print the result, accompanied by an encouraging message. Finally, the program should determine if the sum is a prime number and notify the user with an appropriate message. The goal is to make the tool both enjoyable and informative, allowing the user to explore their favorite numbers in a fun and interactive way, while also introducing some interesting logical checks.

[Back to contents of table](#contents-of-table)

### This assignment aims to evaluate your grasp of the Python fundamentals discussed during our onsite sessions. The topics covered include:

- Print statements
- Strings
- f-Strings
- Operators
- Lists
- Tuples
- For loops
- Input handling

[Back to contents of table](#contents-of-table)

### According to Python Programming Assignment 07:

### This is function to cover the stpes:

> The user for their name and their three favorite numbers.

```python
def is_prime(n):

    """Check if a number is prime."""

    if n <= 1:

        return False

    for i in range(2, int(n**0.5) + 1):

        if n % i == 0:

            return False

    return True


def main():

```

[Back to contents of table](#contents-of-table)

### Step 1: Gather user information

```python
 # Step 1: Gather user information

    name = input("Hello! What's your name? ")

    print(f"Nice to meet you, {name}!")

```
[Back to contents of table](#content-of-table)

### Step 2: Store Numbers in a List

Store the three favorite numbers in a list.

```python
# Step 2: Store numbers in a list

    numbers = []

    for i in range(3):

        num = int(input(f"Please enter your favorite number #{i + 1}: "))

        numbers.append(num)
```

[Back to contents of table](#contents-of-table)

### Step 3: Check Even or Odd

Create a separate list of tuples to store each number along with whether it is "even" or "odd".

```python
# Step 3: Check even or odd

    even_odd_list = [(num, "even" if num % 2 == 0 else "odd") for num in numbers]


```

[Back to contents of table](#contents-of-table)

### Step 4: Create Tuples of Numbers and Their Squares

Use a loop to create tuples containing each number and its square.

```python
# Step 4: Create tuples of numbers and their squares

    squares_list = [(num, num ** 2) for num in numbers]

```

[Back to contents of table](#contents-of-table)

### Step 5: Calculate the Sum of the Numbers

Calculate the sum of the three numbers and print an encouraging message.

```python
# Step 5: Calculate the sum of the numbers

    total_sum = sum(numbers)

    print(f"\nThe sum of your favorite numbers is: {total_sum}. Keep it up, {name}!")


```

[Back to contents of table](#contents-of-table)

### Step 6: Check if the Sum is Prime

Implement a function to check if the sum is a prime number and notify the user.

```python
# Step 6: Check if the sum is prime

    if is_prime(total_sum):

        print(f"Wow, {total_sum} is a prime number! That's awesome!")

    else:

        print(f"Oops! {total_sum} is not a prime number, but that's okay!")


```

[Back to contents of table](#contents-of-table)

### 7: Display even/odd and squares

```python

# Display even/odd and squares

    print("\nHere's a fun summary of your numbers:")

    for num, status in even_odd_list:

        print(f"Number: {num} is {status}.")



    print("\nAnd here are your numbers with their squares:")

    for num, square in squares_list:

        print(f"{num} squared is {square}.")


if __name__ == "__main__":

    main()
```

[Back to contents of table](#contents-of-table)

# 8: complete code available on just one click

> complete the code is available relating to Python Programming Assignment-7

```python
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
        print(f"Wow, {total_sum} is a prime number! That's awesome!")
    else:
        print(f"Oops! {total_sum} is not a prime number, but that's okay!")

    # Display even/odd and squares
    print("\nHere's a fun summary of your numbers:")
    for num, status in even_odd_list:
        print(f"Number: {num} is {status}.")

    print("\nAnd here are your numbers with their squares:")
    for num, square in squares_list:
        print(f"{num} squared is {square}.")

if __name__ == "__main__":
    main()

```

[Back to contents of table](#contents-of-table)

# 9: Jahanzaib Tayyab Github-portal

[Referance: Python Programming Assignment: Number Exploration Tool on JahanzaibTayyab github account. ](https://github.com/JahanzaibTayyab/Batch-62/blob/main/python-learning/assignments/Number_Exploration_Tool.md)

[Back to contents of table](#contents-of-table)
