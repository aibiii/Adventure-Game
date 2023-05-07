import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    global enemy
    villain = [
        "big zombies", "zombie dogs", "zombies without hands", "zombies"]
    enemy = random.choice(villain)
    print_pause("Welcome to an alternate universe!")
    print_pause(
        "The apocalypse with walking dead occurred"
        " as a result of a scientific error."
    )
    print_pause("You are injured, you urgently need to treat the wound!")
    print_pause("Search for medicine. You can either go to house or hospital")


def play_again():
    response = input("Would you like to play again?\n").lower()
    if "no" in response:
        print_pause("Thank you for playing. See you!")
    elif "yes" in response:
        print_pause("Restarting the game...")
        play_game()
    else:
        print_pause("Please enter yes or no.")
        play_again()


def valid_input(prompt, choice):
    while True:
        choice = input(prompt).lower()
        if choice in prompt:
            return choice
        print_pause(f'Sorry, the option "{choice}" is invalid.')


def fight(items):
    choice = valid_input("Would you rather shoot or distract them?\n", [
        "shoot", "distract"]).lower()
    if "shoot" in choice:
        print_pause(
            "That was a mistake! By shooting you attracted"
            " more zombies due to the noise!"
        )
        print_pause("You didn't survive")
        play_again()

    elif "distract" in choice:
        print_pause("Great! You distracted them")
        print_pause(
            "You walked further down the hallway"
            " and got the medicine chest."
        )
        print_pause("Go HOME asap")
        items.append("medicine")
        adventure(items)


def choice_1(items):
    print_pause("You are at home.")
    if "medicine" in items:
        print_pause("Congratulations, you returned safely!")
        print_pause("You got the medicine and survived!")
    else:
        print_pause(
            "Oh, no! There is no medicine chest"
            " in the house, you didn't survive."
        )
    play_again()


def choice_2(items):
    if "medicine" in items:
        print_pause("There's no need to go there again")
        print_pause("You have your medicine chest already")
        adventure(items)
    else:
        print_pause("You are in hospital.")
        print_pause(f"Two {enemy} are standing a couple of meters from you")
        print_pause("You have a gun and empty cans in you backpack")
        fight(items)


def adventure(items):
    print_pause("Enter 1 to go to the house")
    print_pause("Enter 2 to go to hospital")

    run = input("Where would you like to go?\n")
    if run == "1":
        choice_1(items)
    elif run == "2":
        choice_2(items)
    else:
        print_pause("Please enter 1 or 2.")
        adventure(items)


def play_game():
    items = []
    intro()
    adventure(items)


play_game()
