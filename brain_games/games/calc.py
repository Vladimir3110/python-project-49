from brain_games.cli import welcome_user
import random


def calc_game():
    print("brain-calc\n")
    name = welcome_user()
    print("What is the result of the expression?")

    count = 0
    while count < 3:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(["+", "-", "*"])
        expression = f"{num1} {operator} {num2}"
        correct_answer = eval(expression)

        print(f"Question: {expression}")
        user_answer = int(input("Your answer: "))

        if user_answer == correct_answer:
            print("Correct!\n")
        else:
            print("'" + user_answer + "' is wrong answer ;(. Correct answer was"
                                      " '" + correct_answer + "'.")
            print("Let's try again, " + name + "!")

    print(f"Congratulations, {name}!")


calc_game()
