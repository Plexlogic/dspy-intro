import os
import dspy

# We first need to tell dspy which language model we want to use
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
language_model = dspy.OpenAI(model="gpt-4-turbo", api_key=OPENAI_API_KEY)
dspy.settings.configure(lm=language_model)

# We describe our intent with the signature
signature = "name -> welcome_greeting"

# We combine the 'intent' with a prompting technique
predict_module = dspy.Predict(signature)

# Now we can use it

name = input("what is your name?\n")

welcome_greeting = predict_module(name=name)

print(welcome_greeting)
