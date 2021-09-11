import random as r

message = input("What message would you like to encode?(Only letters will be switched)(Capital and lowercase letters are considered to be different characters): ")

given_character = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t",'u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

letter_choice = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t",'u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

new_letter_order = []

encode_message = []

for x in given_character:
    y = r.choice(letter_choice)
    new_letter_order.append(y)
    letter_choice.remove(y)

for character in message:
    for letter in given_character:
        if character == letter:
            new_letter = new_letter_order[given_character.index(letter)+1]
            encode_message.append(new_letter)



encode_message = tuple(encode_message)
stri = ""
for x in encode_message:
    stri = stri + x

print(stri)
