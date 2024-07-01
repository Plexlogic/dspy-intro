from dotenv import load_dotenv
import os
import dspy

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

def use_openai_model(model, max_tokens):
    language_model = dspy.OpenAI(
        model=model,
        api_key=OPENAI_API_KEY,
        max_tokens=max_tokens,
    )
    dspy.settings.configure(lm=language_model)
