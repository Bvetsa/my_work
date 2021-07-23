
def compute_lcm(x, y, z, a):
    greater = 1

    while(True):
       if((greater % x == 0) and (greater % y == 0) and (greater % z == 0) and (greater % a == 0)):
           lcm = greater
           break
       greater += 1

    return lcm

num1 = int(input("Gimme a number: "))
num2 = int(input("Gimme another number: "))
num3 = int(input("Gimme another number: "))
num4 = int(input("Gimme another number: "))

print("The L.C.M. is", compute_lcm(num1, num2, num3, num4))