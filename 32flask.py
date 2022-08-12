import requests
response = requests.get("http://localhost:5001")
expected = "hello  and welcome to the world of games"
actual = response.text
assert expected == actual