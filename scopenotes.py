#Local scope:
#variables are called from the scope they are created from. Ex. if there is an x in the beginning of the program but there is a function with an x that has a different value, the funtion call will use the function's x while anything outside of the function will use the origional x.
#if you are in a function you can put "global" infront and the local variable will become a global variable

#Global Scope
#if no local scope is made, the fuction will use the origional x

# certain classes if edited in a function will effect the global scope and not just the local scope.


x = { "1": "10","2": "20","3": "30"}

def dictfunc(x):
    x["1"] = ("11")
    y = x.get("1")
    print(y)
    print(x)

dictfunc(x)

print(x)

