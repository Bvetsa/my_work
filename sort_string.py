string = ["hello", "my", "name", "is", "bhargava", "i", "like", "to", "play", "games", "videos", "reddit", "annoying", "playful"]

string_len = []

sort_string = []

for x in string:
    string_len.append(len(x))


for x in range(len(string_len)):
    minimum = x
    for y in range(x+1, len(string_len)):
        if (string_len[y] < string_len[minimum]):
            minimum = y  
    temp = string_len[x]
    string_len[x] = string_len[minimum]
    string_len[minimum] = temp

string_len = set(string_len)

for x in string_len:
    for i in string:
        if x == len(i):
            sort_string.append(i)

print(sort_string)