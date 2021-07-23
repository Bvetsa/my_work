x = 0
y = 3
while x <= 100:
    x += 1
    if x % y == 0:
        continue
    print(x)

print("Done")