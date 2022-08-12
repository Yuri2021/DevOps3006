def get_age()
    age = int(input("enter youar age:"))
    if age < 0:
        raise ValueError("age can not be negative")

try:
    get_age()
except ValueError as e:
    if len(e.args) == [0]
    if e.args[0] == "age can not negative"