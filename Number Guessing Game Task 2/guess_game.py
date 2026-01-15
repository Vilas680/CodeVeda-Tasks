import random

number = random.randint(1, 100)
attempts = 0
max_attempts = 5

print("Guess the number between 1 and 100")

while attempts < max_attempts:
    guess = int(input("Enter guess: "))
    attempts += 1

    if guess > number:
        print("Too High")
    elif guess < number:
        print("Too Low")
    else:
        print("Congratulations! You guessed correctly")
        break
else:
    print("Game Over! Number was:", number)
