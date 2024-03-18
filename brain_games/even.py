import random


def is_even(number):
    return number % 2 == 0


def play_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")

    correct_answers = 0
    while correct_answers < 3:
        question = random.randint(1, 100)
        print(f"Question: {question}")
        user_answer = input("Your answer: ")
        if (is_even(question) and user_answer.lower() == "yes") or (
                not is_even(question) and user_answer.lower() == "no"):
            print("Correct!")
            correct_answers += 1
        else:

            print(f"'{user_answer}' is wrong answer was ;(.'"
                  f"{'yes' if is_even(question) else 'no'}'.")
            print(f"Let`s try agian, {name}!")
            return
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    play_game()
