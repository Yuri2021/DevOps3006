import requests
response = requests.get("http://universities.hipolabs.com/search?country=Israel")
print(response.text)
a ="israel"
if a in response.text:
    print()
else:
       print("Israel in list")


