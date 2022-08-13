import re

import requests
import json
#response=requests.get("https://randomuser.me/api/").json()
#print(response.text)
# third-party HTTP client library
import requests

# assume that "app" below is your flask app, and that
 #"Response" is imported from flask.
import requests
import enum
import sre_compile
import sre_parse
import functools

from flask import Flask, request
from requests import Response

app = Flask("Age")






#x = requests.get('http://10.100.102.10:5002/whatismyname')
#print(x.text)
import re

#class RequestBodyModel():
  #name: str
  #nickname: [str]

# Example2: request body only
@app.route('/age', methods=['GET', 'POST'])
def hallo():


 x = requests.get('https://api.agify.io/?name=/')
 personId = request.form.get('personId', type=int)
 print(personId)

app.run(host="0.0.0.0", port=5003, debug=False)
