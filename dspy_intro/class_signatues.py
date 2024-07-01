"""
signatures don't have to be strings we can also implement then with a class
"""

import dspy
from utils.settings import OPENAI_API_KEY

# We first need to tell dspy which language model we want to use
language_model = dspy.OpenAI(model="gpt-4-turbo", api_key=OPENAI_API_KEY)
dspy.settings.configure(lm=language_model)


class CreateGreeting(dspy.Signature):
    """
    An over the top signature which makes the person feel special
    """

    name = dspy.InputField(desc="The name of the person")
    welcome_greeting = dspy.OutputField(desc="An over the top welcome greeting")


module = dspy.Predict(CreateGreeting)

name = input("what is your name?\n")

welcome_greeting = module(name=name)

print(welcome_greeting)
