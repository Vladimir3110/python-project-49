from brain_games.cli import welcome_user
import random
import math


def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    question = f"Question: {num1} {num2}"
    return question, math.gcd(num1, num2)


def gcd_game():
    print("brain-gcd")
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")

    correct_answers = 0
    while correct_answers < 3:
        question, correct_answer = generate_question()
        print(question)
        user_answer = int(input("Your answer: "))
        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f""
                  f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        print(f"Congratulations, {name}!")


if __name__ == '__main__':
    gcd_game()
