my_file = open("random.txt","a")

print(my_file.read)

my_file.write("\n" + (input("What would you like to put in the file?: ")))

my_file.close()

my_file = open("random.txt", "r")

print(my_file.read())