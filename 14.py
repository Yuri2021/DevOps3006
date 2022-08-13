import ast
my_file = open("config.json")
c = dict(ast.literal_eval(my_file.read()))   # create dictionary from my_file, ast convert file to python object
if c["name"] =="aviel":
     print("aviel")

with open("names.txt") as my_file:
    for name in my_file.readlines():
        print(name.strip())   #strip מוריד \\ ורווחים

