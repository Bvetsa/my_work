def rock_paper_scissors():
    import time
    import random
    choices = ("rock","paper","scissors")
    print("Lets play rock, paper, scissors!")
    play = input("Are you ready to play?(y/n) ")
    if play == "y" or play == "Y":
        print("rock")
        time.sleep(0.5)
        print("paper")
        time.sleep(0.5)
        print("scissors")
        time.sleep(0.5)
        print("shoot!")
        time.sleep(0.5)
        print(random.choice(choices))

#rock_paper_scissors()

def num_guess():
    import time
    import random
    array = []
    print("Lets play Number Guesser!")
    play = input("Are you ready to play?(y/n) ")
    if play == "y" or play == "Y":
        x = int(input("What would you like to be the range of this number guesser? "))
        for i in range(1, x + 1):
            array.append(i)
        num = random.choice(array)
        time.sleep(1)
        print("I have my number.")
        time.sleep(0.5)
        print("You have 5 guesses.")
        guess_1 = int(input("What is your first guess? "))
        if guess_1 == num:
            print("You got it correct! the number was " + str(num))
        else:
            guess_2 = int(input("What is your second guess? "))
            if guess_2 == num:
                print("You got it correct! the number was " + str(num))
            else:
                guess_3 = int(input("What is your third guess? "))
                if guess_3 == num:
                    print("You got it correct! the number was " + str(num))
                else:
                    guess_4 = int(input("What is your fourth guess? "))
                    if guess_4 == num:
                        print("You got it correct! the number was " + str(num))
                    else:
                        guess_5 = int(input("What is your fifth guess? "))
                        if guess_5 == num:
                            print("You got it correct! the number was " + str(num))
                        else:
                            if guess_1 != num and guess_2 != num and guess_3 != num and guess_4 != num and guess_5 != num:
                                print("You lost. The number is " + str(num))

num_guess()