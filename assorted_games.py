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
        y = int(input("What would you like to be the min of this number guesser? "))
        x = int(input("What would you like to be the max of this number guesser? "))
        for i in range(y, x + 1):
            array.append(i)
        num = random.choice(array)
        time.sleep(1)
        print("I have my number.")
        time.sleep(0.5)
        print("You have 5 guesses.")
        for x in range(1,5):
            if x == 1:
                y = "st"
            elif x == 2:
                y = "nd"
            elif x == 3:
                y = "rd"
            else:
                y = "th"
            i = int(input("What is your " + str(x) + str(y) + " guess? "))
            if i == num:
                print("You got it correct! the number was " + str(num))
                break
            elif x == 4:
                n = num - i
                if n < 0:
                    n*=-1
                guess_5 = int(input("This is your 5th guess so I will give you a clue. Your last guess was " + str(n) +  " away from the correct answer. What is your fifth guess? "))
                if guess_5 == num:
                    print("You got it correct! the number was " + str(num))
                else:
                    print("You lost. The number is " + str(num))

num_guess()
