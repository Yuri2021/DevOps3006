import requests
print("moshe")
try:
    f = int(input("enter number: "))
    r = 5 / 0
except BaseException as e:
    print("something went wrong, here is more")
    print(e.args)
except ZeroDivisionError:
    print("could not divide by zero")
except ValueError:
    print("enter a legal number")

print("haim")