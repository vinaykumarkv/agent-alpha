from openai import OpenAI
import os

class LLMClient:
    def __init__(self):
        self.client = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')
        #self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = "phi3:mini"

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
