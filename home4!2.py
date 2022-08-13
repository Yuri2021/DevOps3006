import requests
import json
import numpy
import route as route

#response = requests.get('https://api.agify.io/?name=')
#response = requests.get('https://api.agify.io/?name={"[{"name":"moshe","age":70,"count":233482},{"name":"natan","age":36,"count":34742},{"name":"anton","age":36,"count":35010}]"}')
#print(response.text)
#data=response.text
#name = "moshe\n"+"natan\n"+"anton"
#if name in response:
# print()
#else:
#print(name)




from flask import Flask, request

app = Flask("something")

response = requests.get("https://api.agify.io/?name=/")
@app.route('/whatismyname', methods=['GET', 'POST', 'DELETE'])
def hello():
    if request.method == 'GET':
        return '<pre style="word-wrap: break-word; white-space: pre-wrap;">{"name":"moshe","age":70,},{"name":"tom","age":36},{"name":"yosef","age":36}" < / pre >'


    elif request.method == 'POST':
       return "saved new name"
   # if request.method =='POST'and "age"in range(120):




@app.route('/')
def my_func():


   #return "new name insert"
   if request.method == 'GET':
       response = requests.get("https://api.agify.io/?name=/")





       return '<pre style="word-wrap: break-word; white-space: pre-wrap;">{"AGE TESTED GOOD"}" < / pre >'

@app.route('/age', methods=['GET', 'POST'])
def age_fun():
    if request.method == 'GET':
      requests.get("https://api.agify.io/?name=/")
      input(age_fun)


















      #return '<pre style="word-wrap: break-word; white-space: pre-wrap;">{""},{"age":70}< / pre >'



app.run(host="0.0.0.0", port=5005, debug=False)




