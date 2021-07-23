'''
Pseudo code: 

check if there are any ones within the list
if there is a one, add it to the sorted list
check if there are any 2s in the list
if there is a 2, add it to the list
keep going
'''
'''
list_num = [100,3,23,4,1,200]
number = 0
sorted_list = []
num_of_iter = 0



while len(list_num) > 0:
    for x in list_num:
        num_of_iter += 1
        if x == number:
            sorted_list.append(x)
            list_num.remove(x)
            
            
    number = number + 1


print(sorted_list)
print(num_of_iter)
'''
'''
Pseudo code2:

Assumes that the smallest number is the first number
compares to the other numbers via checking if one is smaller(using < operator) than the other
if one is smaller, it swappes the index points to switch where the smaller and bigger numbers are
same for the second number
then third
etc.
'''

array = [3.9,1400,0,50,2,100,-8,4]
'''

for x in range(len(array)):
    minimum = x
    for y in range(x+1, len(array)):
        if (array[y] < array[minimum]):
            minimum = y  
    temp = array[x]
    array[x] = array[minimum]
    array[minimum] = temp

print(array)
'''


