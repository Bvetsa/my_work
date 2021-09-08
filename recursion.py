
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

print(fact(3))


def power(a,b):
    if b == 0:
        return 1
    else:
        return power(a,b-1) * a

print(power(2,10))

def website(a):
    import requests
    import webbrowser
    try:
        r = requests.get(a)
        print(r)
        print("URL is valid and exists on the internet")
        webbrowser.open(a)
    except:
        print("URL does not exist on Internet")
        website(input("What URL would you like to look for. "))

website(input("What URL would you like to look for. "))
