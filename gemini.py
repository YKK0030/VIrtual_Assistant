
import google.generativeai as genai

class Gemini:
    def __init__(self, api_key, model_name):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)

    def generate_code(self, prompts):
        responses = []
        for prompt in prompts:
            response = self.model.generate_content(prompt)
            responses.append(response.text)
        return responses