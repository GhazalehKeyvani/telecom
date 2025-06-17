import requests
import json  # Import JSON separately

url = "http://localhost:11434/api/generate"
data = {
    "model": "qwen2:1.5b",
    "prompt": "چرا آسمان آبی است؟"
}

response = requests.post(url, json=data, stream=True)

final_output = ""
for line in response.iter_lines():
    try:
        json_data = json.loads(line.decode("utf-8"))  # Correct usage
        final_output += json_data.get("response", "")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")  # Handle malformed lines

print(final_output)
