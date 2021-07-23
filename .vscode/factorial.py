give_numv = input("Give me the number: ")
numb = int(give_numv)
ans = (1)
num_str = []

for x in range(1,numb + 1):
    ans = x * ans
    x = x + 1 
    num_str.append(ans)

print("Factorial of " + (give_numv + " is: " + ans)

for x in num_str:
    ans = x * ans

print(ans)

    