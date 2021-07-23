import urllib.request

url = urllib.request.urlopen("http://www.google.com")

#print("Code result is: " + str(url.getcode))
'''
data = url.read()
print(data)
print(type(data))
'''
data = "aaaab ;cd123"
num = 0
for x in data:
    if x.isnumeric() is True:
        print(x)
'''
a = 0

for x in data:
    if x == "a":
        a = a + 1

print(a)
'''
'''

#print(len(data))


a = 0
data_array = []

for x in data:
    data_array.append(x)

for x in data_array:
    if x == "a":
        a = a + 1

print("There are " + str(a) + " A's in data")
'''
'''
count = {}

for character in data:
    if character in count.keys():
        count[character] = count[character] + 1
    else:
        count[character] = 1        

for character in count.keys():
    print( str(character) + ": " + str(count[character] ) )
'''
