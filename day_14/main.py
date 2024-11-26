import game_data
import art
import random

def format_dictionary(person):
    """takes a dictionary with keys 'name', 'description' and 'country' and returns a formatted string"""
    return f" {person['name']}, a {person['description']}, from {person['country']}."

def compare(person1, person2, choice):
    if person1['follower_count'] > person2['follower_count']:
        correct_answer = 'a'
    else:
        correct_answer = 'b'

    if choice == correct_answer:
        return True  # Correct choice
    else:
        return False  # Incorrect choice


def higher_lower():
    person_b = random.choice(game_data.data)
    score = 0
    game_active = True
    first_round = True

    while game_active:
        print(art.logo)

        if not first_round:# Only show score after the first round
                print(f"Correct! Your score is {score}.")


        person_a = person_b
        person_b = random.choice(game_data.data)

        while person_a == person_b:
            person_b = random.choice(game_data.data)

        print(f"Compare A:{format_dictionary(person_a)}")
        print(art.vs)
        print(f"Against B:{format_dictionary(person_b)}")

        guess = input(f"Who has more followers? Type 'A' or 'B':").lower()
        if compare(person_a,person_b,guess):
            score += 1
            print("\n" * 20)
        else:
            print("\n" * 30)
            print(art.sad)
            print(f"Wrong! Game over. Your final score is {score}.")
            game_active = False

        if first_round:
            first_round = False
higher_lower()

again = input("Do you want to play again? 'Y' or 'N':").lower()
if again == 'y':
    higher_lower()
else:
    print("See you soon")





