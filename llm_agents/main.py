import requests

url = "http://103.75.197.35:11434"
headers = {"Content-Type": "application/json"}
data = {"prompt": "سلام، دنیای LLM"}

response = requests.post(url, json=data, headers=headers)
print("Status Code:", response.status_code)
print("Response:", response.text)
