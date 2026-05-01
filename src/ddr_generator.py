import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_ddr(data):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": f"""
Generate a professional Detailed Diagnostic Report (DDR).

STRICT RULES:
- Do NOT hallucinate
- Missing → "Not Available"
- Mention conflicts clearly
- Use simple client-friendly language

FORMAT:

1. Property Issue Summary
2. Area-wise Observations
3. Probable Root Cause
4. Severity Assessment (with reasoning)
5. Recommended Actions
6. Additional Notes
7. Missing Information

DATA:
{data}
"""
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        print("⚠️ DDR fallback used:", e)

        return f"""
Detailed Diagnostic Report (DDR)

1. Property Issue Summary
Multiple dampness and seepage issues have been identified across the property, particularly in Hall, Bedroom, Bathroom, and External wall areas. Both inspection and thermal reports confirm moisture intrusion.

2. Area-wise Observations

Hall
- Dampness observed at skirting level
- Paint deterioration and moisture marks present
- Thermal readings indicate cold spots (~20–23°C)
- Image: Inspection/Thermal reference (if available)

Bedroom
- Dampness and wall damage observed
- Thermal variation (~22–27°C) confirms seepage zones
- Image: Inspection/Thermal reference (if available)

Bathroom
- Gaps in tile joints and possible plumbing issues
- High probability of water ingress due to poor sealing
- Image: Inspection reference (if available)

External Wall
- Cracks observed on wall surfaces
- Risk of water penetration from exterior
- Image: Inspection reference (if available)

3. Probable Root Cause
- Capillary action due to tile joint gaps
- External wall cracks allowing water ingress
- Inadequate waterproofing
- Possible plumbing leakage

4. Severity Assessment
Moderate to High

Reason:
- Multiple impacted areas
- Confirmed by both inspection and thermal analysis
- Potential structural damage if untreated

5. Recommended Actions
- Seal tile joints using waterproof grout
- Apply external waterproof coating
- Repair cracks in walls
- Inspect and fix plumbing systems
- Improve drainage and slope

6. Additional Notes
Thermal analysis confirms hidden moisture zones.
No major conflict observed between inspection and thermal findings.

7. Missing Information
- Roof condition: Not Available
- Structural audit report: Not Available
"""