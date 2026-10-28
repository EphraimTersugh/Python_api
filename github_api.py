import requests

url = "https://api.github.com"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    #print(data)
    print("API requests successful!")
    print("GitHub documentation:", data["notifications_url"])

except requests.RequestException as error:
    print(f"something went wrong: {error}")