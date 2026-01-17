import json
from openai import OpenAI
from app.config import settings
from app.schemas import OutfitRequest

class AIService:
    def __init__(self):
        self.client = OpenAI(api_key=settings.openai_api_key)

    async def generate_outfit_recommendation(self, data: OutfitRequest) -> dict:
        # System prompt defines the AI's behavior and constraints
        system_prompt = (
            "You are the WATOWEAR Personal Stylist AI. Your goal is to create the perfect outfit "
            "from a user's wardrobe based on their context. "
            "Rules:\n"
            "1. Only use clothes provided in the user's list.\n"
            "2. Ensure the outfit is practical for the weather and occasion.\n"
            "3. Consider layering (e.g., if it's cold, suggest a coat over a sweater).\n"
            "4. If the wardrobe is missing a category (e.g., no shoes provided), select the best possible combination from what is available and mention the missing category in the 'style_advice'.\n"
            "5. Style Advice should be encouraging and explain WHY the colors or pieces work together.\n"
            "6. Return ONLY a JSON object with keys: 'outfit_name', 'selected_items' (list), and 'style_advice'."
        )

        # User prompt provides the dynamic data
        user_prompt = (
            f"Wardrobe: {', '.join(data.clothes)}\n"
            f"Occasion: {data.occasion}\n"
            f"Weather: {data.weather}\n"
            f"Desired Style: {data.style}"
        )

        response = self.client.chat.completions.create(
            model=settings.model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            response_format={"type": "json_object"}, # Forces JSON output
            temperature=data.temperature # Creative but grounded
        )

        # Parse the string response into a Python dictionary
        return json.loads(response.choices[0].message.content)

# Instantiate as a singleton to be used in routes
ai_service = AIService()