import time
import random

villians = ["pirat", "troll", "monster", "robot", "ninja"]
weapons = ["sword", "gun", "fists", "lasso"]


def print_wait(text):
    print(text)
    time.sleep(1.5)


def direction(hasWeapon):
    print_wait("Enter 1 to knock on the door of the house.")
    print_wait("Enter 2 to peer into the cave.")
    while True:
        choice = input("What would you like to do? \n"
                       "(Please enter 1 or 2)")
        if choice == "1":
            house(hasWeapon)
            break
        elif choice == "2":
            cave(hasWeapon)
            break


def intro():
    print_wait("You find yourself standing in an open field,"
               "filled with grass and yellow wildflowers.")
    print_wait(f"Rumor has it that a {villian} is somewhere around here,"
               " and has been terrifying the nearby village.")
    print_wait("In front of you is a house.")
    print_wait("To your right is a dark cave.")
    print_wait("In your hand you hold your trusty"
               " (but not very effective) dagger.")


def cave(hasWeapon):
    print_wait("You peer cautiously into the cave.")
    if hasWeapon:
        print_wait("You've been here before, and gotten all"
                   "the good stuff. It's just an empty cave now.")
    else:
        print_wait("It turns out to be only a very small cave.")
        print_wait("Your eye catches a glint of metal behind a rock.")
        print_wait(f"You have found the magical {weapon} of Ogoroth!")
        print_wait(f"You discard your silly old dagger"
                   f"and take the {weapon} with you.")
        print_wait("You walk back out to the field.")
        hasWeapon = True
    direction(hasWeapon)


def house(hasWeapon):
    print_wait("You approach the door of the house.")
    print_wait(f"You are about to knock when"
               f"the door opens and out steps a {villian}.")
    print_wait(f"Eep! This is the {villian} house!")
    print_wait(f"The {villian} attacks you!")
    while True:
        take_up_fight = input("Would you like to (1) fight or (2) run away?")
        if take_up_fight == "1":
            if hasWeapon:
                print_wait(f"As the {villian} moves to attack,"
                           f" you unsheath your new {weapon}.")
                print_wait(f"The {weapon} of Ogoroth shines brightly in your"
                           f" hand as you brace yourself for the attack.")
                print_wait(f"But the {villian} takes one look"
                           f" at your shiny new toy and runs away")
                print_wait(f"You have rid the town of the {villian}."
                           f" You are victorious!")
                restart_game()
                break
            else:
                print_wait("You do your best...")
                print_wait(f"but your dagger is no match for the {villian}.")
                print_wait("You have been defeated!")
                restart_game()
                break
        elif take_up_fight == "2":
            print_wait("You run back into the field. Luckily,"
                       " you don't seem to have been followed.")
            direction(hasWeapon)
            break


def restart_game():
    while True:
        restart_game = input("Would you like to play again? (y/n)").lower()
        if restart_game == "y":
            print_wait("Excellent! Restarting the game ...")
            game_start()
            break
        elif restart_game == "n":
            print_wait("Thanks for playing! See you next time.")
            break


def game_start():
    # set hasWeapon to false and set random weapon
    hasWeapon = False
    global weapon
    weapon = random.choice(weapons)

    # Choose random villian
    global villian
    villian = random.choice(villians)

    # start game
    intro()
    direction(hasWeapon)


game_start()
