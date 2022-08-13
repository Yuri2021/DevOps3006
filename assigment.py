x = 20
y = 30
if x > y:
    print("BIG")
else:
    print("SMALL")

for x in range(5):
    print(x)

season = 1
if season == 1:
    print("summer")
elif season == 2:
    print("winter")
elif season == 3:
    print("fall")
elif season == 4:
    print("spring")

count = 1
while count < 11:
    print(count)
    count = count + 1

age = 25
letter = "g"
currency = 3.52
flew = True
apartment_number = 20

print(age)
print(letter)
print(currency)
print(flew)
print(apartment_number)
print(currency + age)

number = input("Enter your phone number: ")
print("Phone number", number)


def printHello():
    print("hello")


def calculate():
    print(5 + 3.2)

def print_name(name):
    print(name)

def divide_number(num):
        print(num/2)


# Function to demonstrate printing pattern
def pypart(n):
    # outer loop to handle number of rows
    # n in this case
    for i in range(0, n):

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            # printing stars
            print("* ", end="")

        # ending line after each row
        print("\r")


# Driver Code
n = 5
pypart(n)

