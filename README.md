# WATOWEAR - Technical Exercise

### ⏱️ Timing
- **Start**: 17/01/2026 10:27h
- **Finished**: 17/01/2026 11:52h

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

Multi-Agent Validation Loop: To eliminate logic gaps. I would implement a "Critic" agent. This second AI layer validates the Stylist's output against a strict "Practicality Checklist" and triggers a regeneration if the outfit doesn't meet the activity's physical requirements.

RAG (Retrieval-Augmented Generation): Instead of relying solely on the LLM's internal knowledge, I would integrate a Vector Database (e.g., Pinecone or Weaviate) containing curated expert fashion rules and seasonal trends. This would "ground" the AI’s suggestions in professional styling principles.

Vision Integration (LMM): Upgrading to a multi-modal model (like GPT-4o or Gemini 1.5 Pro) to allow users to upload photos of their clothes. The system would then use visual features (texture, exact color hex codes, and patterns) rather than just text descriptions