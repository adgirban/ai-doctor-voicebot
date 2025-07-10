import os
import base64
import fireworks
from fireworks import LLM
from dotenv import load_dotenv

load_dotenv()

FIREWORKS_API_KEY=os.getenv("FIREWORKS_API_KEY")
fireworks.client.api_key = FIREWORKS_API_KEY

image_path="acne.jpg"
image_file=open(image_path, "rb")
encoded_image=base64.b64encode(image_file.read()).decode('utf-8')

llm = LLM(model="qwen2p5-vl-32b-instruct", deployment_type="serverless")
query="Is there something wrong with my face?"
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": query
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64, {encoded_image}", 
                },
            }
        ]
    }
]
chat_completion=llm.chat.completions.create(
    messages=messages,
)

print(chat_completion.choices[0].message.content)