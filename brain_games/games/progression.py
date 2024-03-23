from brain_games.cli import welcome_user
import random


def generate_progression(start, step, length):
    progression = []
    for _ in range(length):
        progression.append(start)
        start += step
    return progression


def hide_element(progression, index):
    hidden_progression = progression.copy()
    hidden_progression[index] = '..'
    return hidden_progression


def play_progression_game():
    print("brain-progression\n")
    name = welcome_user()
    print("What number is missing in the progression?")
    num_correct_answers = 0
    while num_correct_answers < 3:
        start = random.randint(1, 10)
        step = random.randint(1, 10)
        length = random.randint(5, 10)
        progression = generate_progression(start, step, length)
        hidden_index = random.randint(0, length - 1)
        hidden_progression = hide_element(progression, hidden_index)

        question = ' '.join(str(num) for num in hidden_progression)
        correct_answer = str(progression[hidden_index])

        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
            num_correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    play_progression_game()
