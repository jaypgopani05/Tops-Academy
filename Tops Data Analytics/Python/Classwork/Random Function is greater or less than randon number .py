import random

# Generate a random number between 1 and 200.
i = random.randint(1, 200)

while True:
    try:
        number = int(input("Enter a number between 10 and 20: "))
    except ValueError:
        print("❗Please enter a valid number.")
        continue
    if number == i:
        print(f"👍 Correct! You guessed the number: {i}")
        break
    elif number < i:
        print("🤦‍♂️ Too low. Try a higher number.")
    else:
        print("🤦‍♂️ Too high. Try a lower number.")
