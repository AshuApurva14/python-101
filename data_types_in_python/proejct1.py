import requests

response=requests.get("https://api.github.com")

if response.status_code == 200:
    print(f"API  request is successful")
else:
   print(f"API  request failed")

print(f"Response of the API is: {response.status_code} ")
