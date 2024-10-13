import requests
import json

# url = f"https://api.github.com/repos/giampaolo/psutil/contents/"
url = f"https://api.github.com/repos/python-pillow/Pillow/git/trees/main?recursive=1"
# url = f"https://api.github.com/repos/giampaolo/psutil"
response = requests.get(url)

data_str=json.dumps(response.json(),indent=4)

print(data_str)