from brain_games.cli import welcome_user
from brain_games.constant import GAME_INSTRUCTIONS
import random


def is_even(number):
    return number % 2 == 0


def generate_question():
    number = random.randint(1, 100)
    return str(number)


def get_correct_answer(number):
    if is_even(int(number)):
        return 'yes'
    return 'no'


def play_game():
    name = welcome_user()
    print(GAME_INSTRUCTIONS["even"])

    for _ in range(3):
        question = generate_question()
        print("Question: " + question)
        user_answer = input("Your answer: ")
        correct_answer = get_correct_answer(question)

        if user_answer.lower() == correct_answer:
            print("Correct!")
        else:
            print("'" + user_answer + "' is wrong answer ;(. Correct answer was"
                                      " '" + correct_answer + "'.")
            print("Let's try again, " + name + "!")
            return

    print("Congratulations, " + name + "!")
