from dotenv import load_dotenv
load_dotenv()
import os, requests

r = requests.get(
    "https://api.groq.com/openai/v1/models",
    headers={"Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}"},
)
for m in sorted(x["id"] for x in r.json()["data"]):
    print(m)