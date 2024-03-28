from brain_games.cli import welcome_user
from brain_games.constants import GAME_INSTRUCTIONS
import random
import prompt


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def play_prime():
    print("brain-prime\n")
    name = welcome_user()
    print(GAME_INSTRUCTIONS["prime"])

    for _ in range(3):
        number = random.randint(1, 100)
        print(f"Question: {number}")
        user_answer = prompt.string("Your answer: ")
        correct_answer = "yes" if is_prime(number) else "no"

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was "
                  f"'{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
