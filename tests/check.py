import requests

username = "pushpa_sathish"
access_key = "cgubzyOubHatV66TTQyFMyWI2HJZ95psh5HzKiUXYkyFs6Xhmc"
url = f"https://{username}:{access_key}@hub.lambdatest.com/wd/hub/status"

response = requests.get(url)

if response.status_code == 200:
    print("Credentials are valid.")
else:
    print(f"Invalid credentials. Response: {response.text}")
