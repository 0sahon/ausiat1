# This is a guessing the number game.
import random

# User's name
print('Hello! What is your name? ')
myName = input()
print("Hi " + str(myName) + "!" + " Let's play a guessing game.")


def random_game():

    play = True
    while play:

        easy = random.randint(1, 100)
        medium = random.randint(1, 100)
        hard = random.randint(1, 100)
        # prompts the user to select a difficulty to play on
        print("Would you like to play on easy, medium, or hard?"
              "\nType 'e' for easy, 'm' for medium, or 'h' for hard!")

        level_selection = True
        while level_selection:
            level = input()
            if level == "e":
                print("\nAwesome! We'll begin with easy!")
                level_selection = not True
                break
            if level == "m":
                print("\nAwesome! We'll begin with medium!")
                level_selection = not True
                break
            if level == "h":
                print("\nAwesome! We'll begin with hard!")
                level_selection = not True
                break
            else:
                print("Invalid input!\nPlease enter either e, m, or h. ")



        if level == 'e':
            print("Because you selected easy, you'll have 20\nguesses to guess a number between 1-10.")
            guesses_left = 6
            while guesses_left != 0:
                try1 = int(input("So, what's your guess? \n"))
                if try1 == easy:
                    print("You have got it right " + str(easy))
                    print("Congratulations " + str(myName) + "!")
                    break
                elif try1 < easy:
                    print("That was wrong")
                elif try1 > easy:
                    print("That was wrong")
                guesses_left -= 1
                print('You now have ' + str(guesses_left) + ' guesses left!')

                # Fun 6 tries left count down
                if guesses_left == 6:
                    print("Common', you can do this!")
                if guesses_left == 5:
                    print("Common', you can do this!\n\(^ω^\)")
                if guesses_left == 4:
                    print("That's ok, it's on Easy.\n¯\_(ツ)_/¯")
                if guesses_left == 3:
                    print("You're running out of guesses!\nᶘ ")
                if guesses_left == 2:
                    print("Just 2 guesses left. Can the impossible happen?\n( ͡° ͜ʖ ͡°)")
                if guesses_left == 1:
                    print("By the old Gods and the New.\nYou've got 1 guess left.\n😨")

                # If the user runs out of guesses
                if guesses_left == 0:
                    print( "Game over!")

    # If the user selects m for Medium -
        if level == 'm':
            print("Because you selected medium, you'll have 4\nguesses to guess a number between 1-20.")
            guesses_left = 4
            while guesses_left != 0:
                try1 = int(input("So, what's your guess? \n"))
                if try1 == medium:
                    print("That's it, you've guessed the right number! " + str(medium))
                    print("Congratulations " + str(myName) + "!")
                    break
                elif try1 < medium:
                    print("That was wrong")
                elif try1 > medium:
                    print("That was wrong")
                guesses_left -= 1
                print('You now have ' + str(guesses_left) + ' guesses left!')

                
                if guesses_left == 5:
                    print("Common', you can do this!\n\(^ω^\)")
                if guesses_left == 4:
                    print("That's ok, it's on Medium.\n¯\_(ツ)_/¯")
                if guesses_left == 3:
                    print("You're running out of guesses!\n")
                if guesses_left == 2:
                    print("Just 2 guesses left. Can the impossible happen?\n( ͡° ͜ʖ ͡°)")
                if guesses_left == 1:
                    print("By the old Gods and the New.\nYou've got 1 guess left.\n😨")

                # If the user runs out of guesses
                if guesses_left == 0:
                    print( "Game over!")

    # If the user selects h for Hard - 
        if level == 'h':
            print("Because you selected hard, you'll have 3\nguesses to guess a number between 1-50.")
            guesses_left = 3
            while guesses_left != 0:
                try1 = int(input("So, what's your guess? \n"))
                if try1 == hard:
                    print("That's it, you've guessed the right number! " + str(hard))
                    print("Congratulations " + str(myName) + "!")
                    break
                elif try1 < hard:
                    print("That was wrong")
                elif try1 > hard:
                    print("That was wrong")
                guesses_left -= 1
                print('You now have ' + str(guesses_left) + ' guesses left!')

                
                if guesses_left == 3:
                    print("Common', you can do this!\n\(^ω^\)")
                if guesses_left == 2:
                    print("Just 2 guesses left. Can the impossible happen?\n( ͡° ͜ʖ ͡°)")
                if guesses_left == 1:
                    print("By the old Gods and the New.\nYou've got 1 guess left.\n😨")

                # If the user runs out of guesses
                if guesses_left == 0:
                    print( "Game over!")

        maybe_play = True
        while maybe_play:
            again = input("\nWould you care to play again?\nYes or No\n ")
            if again == 'No' or again == 'no':
                print('\nOk, thank you for playing.\nFeel free to come back any time!')
                maybe_play = not True
                play = not True
            elif again == 'yes' or again == 'Yes':
                print("\nCool, let's play again!👍\n")
                maybe_play = not True
                play = True
            else:
                print('Please enter either yes or no.')
                input()
                maybe_play = not True
                play = not True


random_game()