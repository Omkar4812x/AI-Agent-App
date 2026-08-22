import os
import requests
import json

response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": "Bearer " + os.getenv("OPENROUTER_API_KEY", "YOUR_OPENROUTER_API_KEY") + "",
    "Content-Type": "application/json",
    
  },
  data=json.dumps({
    "model": "mistralai/mistral-7b-instruct:free",
    "messages": [
      {
        "role": "user",
        "content": "What is the meaning of life?"
      }
    ],

  })
)

@app.route('/health', methods=['GET'])
def health_check():
    return {'status': 'healthy', 'service': 'AI-Agent-App'}, 200
