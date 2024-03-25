from brain_games.cli import welcome_user
import random


def is_even(number):
    return number % 2 == 0


def play_game():
    name = welcome_user()
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")

    correct_answers = 0
    while correct_answers < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        user_answer = input("Your answer: ")

        if (is_even(number) and user_answer == "yes") or (
                not is_even(number) and user_answer == "no"):
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{'yes' if is_even(number) else 'no'}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    play_game()
