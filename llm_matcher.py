import requests

def is_match(query, title, groq_api_key):
    headers = {
        "Authorization": f"Bearer {groq_api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {
                "role": "user",
                "content": f"Does the following product title match the search query? Reply with YES or NO only.\nQuery: {query}\nTitle: {title}"
            }
        ]
    }

    try:
        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
        result = response.json()["choices"][0]["message"]["content"].strip().upper()
        return result == "YES"
    except Exception as e:
        print("Groq LLM error:", e)
        return False