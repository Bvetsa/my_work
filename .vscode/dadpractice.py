'''
class person:
    def __init__(self, name, age, FavoriteColor):
        self.name = name 
        self.age = age
        self.FavoriteColor = FavoriteColor

    def print_info(self):
        print(self.name + " is " + str(self.age) + " years old.")


john = person("John",33,"orange")
mary = person("Mary", 24, "yellow")


john = child("John","Becker",2016)

class child(person):
    def __init__(self,fname,lname,grad):
        self.fname = fname
        self.lname = lname
        self.grad = grad

john = person("John","Becker",2016)

print(john.fname)

john.print_info()
mary.print_info()
'''
'''
a = ["1","2","3"]
b = ['4','5','6']
c = [a,b]
d = [c,a,b]

print(d)
'''
#s = "Vetsas-MacBook-Pro:python bhargavavetsa$"


'''
for x in s:
    if x == "a":
        a = a + 1

print(a)
'''

''''
for x in s:
    if x in a:
        continue
    a.append(x)

print(a)
'''
'''
first number will be multiplied and will keep going
same will happen to second number 
if in either string there is a number that is in both then program will print
'''