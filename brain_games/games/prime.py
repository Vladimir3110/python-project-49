from brain_games.cli import welcome_user
import random
import math


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def play_prime():
    print("brain-prime\n")
    name = welcome_user()
    print("'yes' if given number is prime. Otherwise answer 'no''.")

    for _ in range(3):
        question = random.randint(1, 100)
        correct_answer = "yes" if is_prime(question) else "no"

        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f""
                  f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    play_prime()
