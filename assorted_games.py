def rock_paper_scissors():
    import time
    import random
    choices = ("rock","paper","scissors")
    print("Lets play rock, paper, scissors!")
    play = input("Are you ready to play?(y/n)")
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

rock_paper_scissors()
