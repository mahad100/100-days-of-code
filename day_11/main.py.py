import random
import os
import art  # Make sure the art module is available in your environment

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear console for Windows or Unix


def deal():
    player_cards = random.sample(cards, 2)  # List with 2 cards for player
    computer_cards = random.sample(cards, 2)  # List with 2 cards for computer

    deal_info = {
        "player_cards": player_cards,  # This is a list
        "player_score": sum(player_cards),  # Sum of player's initial cards
        "computer_cards": computer_cards,  # This is a list
        "computer_score": sum(computer_cards)  # Sum of computer's initial cards
    }

    return deal_info  # Returns dictionary with lists inside


def blackjack_check(player_score, computer_score, player_cards, computer_cards):
    # Check for a blackjack
    if player_score == 21:
        print(f"Your final hand: {player_cards}, final score: {player_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        print("You win 😃")
        return True
    elif computer_score == 21:
        print(f"Your final hand: {player_cards}, final score: {player_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        print("You Lose 😤")
        return True
    return False


def blackjack():
    while True:  # Main loop to allow playing multiple games
        clear_screen()  # Clear the console at the beginning of the game
        print(art.logo)  # Print the logo

        game1 = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if game1.lower() == 'y':
            # Get initial deal
            deal_info = deal()

            # Unpack dictionary values into separate variables
            player_cards = deal_info["player_cards"]
            player_score = deal_info["player_score"]
            computer_cards = deal_info["computer_cards"]
            computer_score = deal_info["computer_score"]

            # Check for an immediate blackjack
            if blackjack_check(player_score, computer_score, player_cards, computer_cards):
                continue  # Restart game if there's an initial blackjack

            # Player's turn to draw
            while True:
                print(f"Your cards: {player_cards}, current score: {player_score}")
                print(f"Computer's first card: {computer_cards[0]}")

                # Player chooses whether to draw another card
                should_draw = input("Type 'y' to get another card, type 'n' to pass: ")
                if should_draw.lower() == 'y':
                    new_card = random.choice(cards)
                    player_cards.append(new_card)  # Add new card to player's list
                    player_score = sum(player_cards)  # Update player's score
                    if player_score > 21:
                        print(f"Your final hand: {player_cards}, final score: {player_score}")
                        print("You went over 21. You lose 😤")
                        break  # End the player's turn since they went over
                else:
                    break  # Player chooses not to draw, end their turn

            # Computer's turn to draw if under 17
            while computer_score < 17:
                new_card = random.choice(cards)
                computer_cards.append(new_card)  # Add new card to computer's list
                computer_score = sum(computer_cards)  # Update computer's score

            # Final result display
            print(f"Your final hand: {player_cards}, final score: {player_score}")
            print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

            # Final comparison after both are done drawing
            if player_score > 21:
                print("You went over. You lose 😤")
            elif computer_score > 21 or player_score > computer_score:
                print("You win 😃")
            elif player_score == computer_score:
                print("It's a draw 😐")
            else:
                print("You lose 😤")
        else:
            print("Maybe next time!")
            break  # Exit the game if the player chooses not to play


blackjack()
