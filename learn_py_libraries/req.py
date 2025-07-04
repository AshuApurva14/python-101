import requests

response = requests.get("https://api.github.com", timeout=2)

if response.status_code == 200:
    print("Success")
elif response.status_code == 400:
    print("Note_Found")

elif response.status_code == 500:
    print("Internal Server Error")

print(f" Status of API is: {response.status_code}")