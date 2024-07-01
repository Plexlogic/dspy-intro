# Tell Python what we're using (e.g., DSPy).
import dspy

# Get our Open AI secret key
from utils.settings import OPENAI_API_KEY

# Tell DSPy which language model to use,
language_model = dspy.OpenAI(
    # in this case ChatGPT 4 Turbo,
    model="gpt-4-turbo",
    # and also give it an API key so it can use your account.
    api_key=OPENAI_API_KEY,
)
dspy.settings.configure(lm=language_model)

# Tell DSPy we're going to give it a `name` and want it to predict a `welcome_greeting`.
predict_module = dspy.ChainOfThought("name -> welcome_greeting")

# Tell DSPy the user's name and make it predict the `welcome_greeting`.
results = predict_module(
    # We will ask the user to input their name
    name=input("what is your name?\n")
).welcome_greeting

# You can change `name` and `welcome_greeting` to something else, like
# `date_of_birth` and `horoscope`. Make sure you change it EVERYWHERE in
# this file, and don't use spaces or other symbols. Programming is very
# unforgiving, so if there are any typos it won't work.

# Display the output.
print(results)
