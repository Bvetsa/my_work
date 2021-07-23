
numb1_array = []
numb2_array = []
numb1 = 3
numb2 = 5
b = 1

for temp in range(1,numb2 + 1):
    temp * b
    b = b + 1
    numb1_array.append(temp*numb1)


for temp in range(1,numb1 + 1):
    temp * b
    b = b + 1
    numb2_array.append(temp*numb2)
print(numb1_array)
print(numb2_array)




for x in range((numb1 + 1) * (numb2 + 1)):
    print(x)
    print(numb1)
    print(numb2)
    if x in str(numb1) and x in str(numb2):
        print (x)