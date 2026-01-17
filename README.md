# WATOWEAR - Technical Exercise

### ⏱️ Timing
- **Start**: 17/01/2026 10:27h
- **Finished**: 

### 🛠 Tech Stack
- **FastAPI**: For high-performance asynchronous API handling.
- **OpenAI API**: Utilizing `gpt-4o-mini` with **JSON Mode** for structured responses.
- **Docker**: Containerized environment for instant deployment.
- **Pytest**: Unit testing with mocking to ensure logic stability without API costs.

### 💡 Product Logic & Technical Choices
1. **Structured Output**: I enforced a JSON schema in the AI prompt. This ensures the frontend always receives a predictable object, preventing "hallucinations" from breaking the app.
2. **Service Layer Pattern**: AI logic is separated from API routes. This makes the code modular and easy to test or swap for another provider (like Gemini or Claude).
3. **Validation**: Used Pydantic to ensure the wardrobe is never empty and context fields are present before hitting the AI.
4. **Temperature Control**: Added a `temperature` parameter to allow the app to toggle between "Safe/Classical" and "Creative/Bold" fashion advice.

### ⚠️ Limits & Future Evolutions
- **Image Recognition**: Currently text-based. In a real app, I'd use a multi-modal model to analyze clothes from photos.
- **Wardrobe Memory**: I would implement a database (PostgreSQL) to save the user's wardrobe so they don't have to send the full list every time.
- **Personalization**: Implementing a "Style Profile" (User preferences like 'Avoid Yellow' or 'Loves Oversized') to refine the AI prompts.

### 🚀 How to Launch
1. Rename `.env.example` to `.env` and add your OpenAI Key.
2. `docker-compose up --build`
3. Test it: `python3 scripts/demo.py`