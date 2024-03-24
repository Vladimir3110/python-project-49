from brain_games.cli import welcome_user
import random


def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2


def calc_game():
    print("\nbrain-calc\n")
    name = welcome_user()
    print("\nWhat is the result of the expression?")

    max_rounds = 3
    correct_answers = 0

    for _ in range(max_rounds):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        operator = random.choice(["+", "-", "*"])
        expression = f"{num1} {operator} {num2}"

        print(f"Question: {expression}")
        user_answer = int(input("Your answer: "))

        correct_answer = calculate(num1, num2, operator)
        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"'{user_answer}' is the wrong answer ;(. "
                f"The correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break

    if correct_answers == max_rounds:
        print(f"Congratulations, {name}!")


calc_game()
