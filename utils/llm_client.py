from openai import OpenAI

import os

class LLMClient:
    def __init__(self):
        llm_key = os.getenv("OLLAMA_KEY")
        llm_url = os.getenv("OLLAMA_BASE_URL")
        llm_model = os.getenv("OLLAMA_MODEL")
        # llm_url = os.getenv("GEMINI_URL")
        # llm_key = os.getenv("GEMINI_API_KEY")
        # llm_model = os.getenv("GEMINI_MODEL")

        self.client = OpenAI(base_url=llm_url, api_key=llm_key)
        self.model = llm_model

    def generate(self, prompt):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an expert industrial field technician."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        
        tokens = response.usage.total_tokens if response.usage else 0

        return response.choices[0].message.content.strip(), tokens
