
print("Which Olimpian are you? Take the quiz to find out!\n")


q1 = input("What would be your ideal vacation?\n1. Tropical beach\n2. Playing Video Games at home\n3. Spending time with your family\n4. Working\n\n")
q2 = input("What is your favorite food?\n1. Cookies\n2. Pizza\n3. Pasta\n4. Noodles\n\n")
q3 = input("What is your favorite animal?\n1. Eagle\n2. Dog\n3. Cat\n4. Deer\n\n")
q4 =input("What is your favorite color?\n1. Red\n2. Blue\n3. Yellow\n4. Green\n\n")
q5 =input("What is your favorite music genre?\n1. Rap\n2. Pop\n3. Indie\n4. Rock\n\n")
q6 =input("What is your favorite holiday\n1. Birthday\n2. Christmas\n3. Hanukhah\n4. Thanksgiving\n\n")
q7 =input("What was your favorite subject in school?\n1. ELA\n2. Science\n3. Math\n4. History\n\n")
q8 =input("What is your dream superpower? \n1. Super Smarts\n2. Speed\n3. Flight\n4. Strength\n\n")
q9 =input("What would your friends describe you as?\n1. Caring\n2. Kind\n3. Cool\n4. Smart\n\n")

n = (q1,q2,q3,q4,q5,q6,q7,q8,q9)


if n == ("2","1","3","3","2","5","2","3","5") or n == ("2","3","5","2","2","2","4","4","1") or n == ("2","2","2","4","1","4","4","2","2"):
    print("You are Zeus!")
elif n == ("3","5","2","3","1","7","5","","") or n == ("3","1","4","5","3","5","2","4","4") or n == ("3","2","5","5","2","3","5","6","6"):
    print("You are Poseidon!")
elif n == ("2","1","3","4","4","1","3","2","1") or n == ("1","3","4","2","2","3","4","2","4") or n == ("2","4","1","2","4","4","2","1","2"):
    print("You are Hades!")
elif n == ("3","2","2","4","2","1","4","2","1") or n == ("3","2","1","3","1","2","4","1","2") or n == ("3","2","2","2","2","4","4","1","2"):
    print("You are Athena!")
elif n == ("1","3","1","3","3","2","2","2","2") or n == ("2","2","2","2","2","2","2","2","2") or n == ("3","3","3","3","3","3","3","3","3"):
    print("You are Haphestus!")
elif n == ("1","1","1","1","1","1","1","1","1") or n == ("4","4","4","4","4","4","4","4","4") or n == ("4","2","1","2","2","3","4","1","2"):
    print("You are Dionysus!")
elif n == ("2","2","2","4","1","2","2","3","1") or n == ("3","1","3","3","3","1","2","2","3") or n == ("1","2","2","3","4","1","2","4","4"):
    print("You are Hera!")
elif n == ("1","3","3","3","3","3","3","3","3") or n == ("1","4","3","2","3","3","2","3","4") or n == ("1","2","3","2","4","3","3","4","2"):
    print("You are Apollo!")
elif n == ("3","3","4","2","1","3","2","3","3") or n == ("2","3","3","3","2","1","4","3","3") or n == ("4","3","2","3","3","4","4","3","2"):
    print("You are Ares!")
elif n == ("3","4","2","1","2","4","2","2","1") or n == ("2","4","3","2","2","3","3","4","5") or n == ("1","4","2","4","1","3","3","4","2"):
    print("You are Artemis!")
elif n == ("2","2","1","3","4","4","2","2","1") or n == ("4","4","3","2","1","2","2","2","4") or n == ("4","3","2","2","2","1","1","2","2"):
    print("You are Aphrodite!")
elif n == ("2","3","1","1","2","3","2","3","1") or n == ("1","1","1","1","2","3","2","3","2") or n == ("2","3","3","1","1","2","2","2","3"):
    print("You are Hermes!")