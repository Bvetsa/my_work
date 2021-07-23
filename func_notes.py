'''
def myfunc(**kid):
  print(kid["fullname"])

myfunc(fname = "Toby",lname = "Harris", fullname = "Toby Harris")
#2 asterix means it can print any of the desired variables
'''
'''
def myfunc1(kid):
  print(kid["fullname"])

myfunc1({"fname":"Toby", "lname":"Harris", "fullname":"toby harris"})
'''
'''
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
#by giving the variable a value when creating it if you dont use a value when calling it will use the already given value
'''