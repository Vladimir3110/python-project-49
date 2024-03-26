from brain_games.cli import welcome_user
import random


def calculate(expression):
    return eval(expression)


def calc_game():
    print("brain-calc\n")
    name = welcome_user()
    print("What is the result of the expression?")

    correct_answers = 0
    for _ in range(3):
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        operator = random.choice(["+", "-", "*"])
        expression = f"{num1} {operator} {num2}"

        print(f"Question: {expression}")
        user_answer = input("Your answer: ")

        correct_answer = calculate(expression)
        if int(user_answer) == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was "
                  f"'{correct_answer}'.")
            print(f"Let's try again, {name}!")
            retur
            break

    print(f"Congratulations, {name}!")
    return


calc_game()
