'''
Pseudo Code:
compares all adjacent numbers(using > or < signs) going left to right throughout the line
keeps iterating again and again until there are no errors when it goes through
'''

list_num = [3,4,2,2,5.218472983,5,1,2,4,-5,212,-1323]

n = len(list_num)
for i in range(n):
    for j in range(0, n-i-1):
        if list_num[j] > list_num[j+1] :
            list_num[j], list_num[j+1] = list_num[j+1], list_num[j]

print(list_num)