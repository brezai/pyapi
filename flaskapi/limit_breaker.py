import requests

for req in range (201):
    r = requests.get("http://0.0.0.0:224/fast")
    print(req, r.status_code)
