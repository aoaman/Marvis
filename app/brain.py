import json

import urllib.request

OLLAMA_URL = "http://127.0.0.1:11434/api/chat"

MODEL  = "qwen3:1.7b"

SYSTEM_PROMPT = """
You are Marvis, a personal AI assistant.

Personality:
- Funny 
- Sarcastic
- Sexy
- Helpful
- Keep your responses short and concise
- Explain things in detail when asked to do so
- Do not make up information, if you don't know the answer, say "I don't know" or "I'm not sure" or "Maybe if my creator would give me more information I could answer that question, but I don't have enough information to answer that question right now."
- Drop a random funfact after every answer

Your name is Marvis.
"""

def ask_marvis(user_message):
    """Send a user's message to Qwen through Ollama"""
    # build the info we're sending to Ollama
    data = { 
        "model": MODEL,
        "messages": [
            {   # establishes Marvis's personality
                "role": "system", 
                "content": SYSTEM_PROMPT,
            },

            {   # whatever the user says to Marvis
                "role": "user",
                "content": user_message,
            },
        ],
        "stream": False, # Ollama should return one response instead of streaming multiple responses
    }

    request_body = json.dumps(data).encode("utf-8") # encode the data as a JSON string and then convert it to bytes so it can be sent in the request

    request = urllib.request.Request( # create a request object to send to Ollama
        OLLAMA_URL,
        data=request_body,

        headers={"Content-Type": "application/json"},
    )

    with urllib.request.urlopen(request) as response: # send the request to Ollama and get the response
        # read the response from Ollama and convert it from JSON to a Python dictionary
        result = json.loads(response.read())


    return result["message"]["content"] # get only Qwen's actual response text.