from brain_games.cli import welcome_user
import random


def calc_game():
    print("brain-calc\n")
    name = welcome_user()
    print("What is the result of the expression?")

    correct_answers_count = 0
    while correct_answers_count < 3:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(["+", "-", "*"])
        expression = f"{num1} {operator} {num2}"
        correct_answer = eval(expression)

        print(f"Question: {expression}")
        user_answer = int(input("Your answer: "))

        if user_answer == correct_answer:
            print("Correct!\n")
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was "
                  f"'{correct_answer}'.")
            print(f"Let's try again, {name}!")
        break
        
        print(f"Congratulations, {name}!")


calc_game()
