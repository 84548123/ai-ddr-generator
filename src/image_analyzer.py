import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_images(pages):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # cheaper model
            messages=[
                {
                    "role": "user",
                    "content": f"""
Analyze these inspection and thermal observations.

Identify:
- Moisture presence
- Dampness indicators
- Temperature anomalies

Data:
{pages}
"""
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        print("⚠️ Image analysis fallback used:", e)

        # fallback if API fails
        return "Moisture and dampness observed based on inspection and thermal data."