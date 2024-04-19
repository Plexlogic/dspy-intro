# An Introduction to DSPy

## What's this?

This is a project for using [DSPy](https://github.com/stanfordnlp/dspy), a technology that writes prompts for LLMs like ChatGPT so you don't even have to do that. You simply tell it what you're giving it, and what you want it to give back.

This project shows you how to make a program which asks for the user's name and creates a greeting for them ("Hello, Plexus!"). You can easily change it to do something else, like ask the user's date of birth and give them a horoscope. Or ask for information about a prospective client and give you a BANT score if you're on the sales team. Or whatever.

## How does it work?

If you'd like to become an *engineeer* and start experimenting with AI, you will need to:

1. Ask Christian for an invite to our Open AI account so you can log in
1. Log in to Open AI and go to your secret keys at https://platform.openai.com/api-keys
1. Click **Create new secret key**, give it a name, and write it down. It will look something like this:
   `sk-proj-ExampleKeyExampleKeyExampleKeyExampleKeyExampleK`.

   **Important**: You secret keys are like passwords, and should never be shared (especially online).
1. Time for some engineering (this will work on Mac only).
   1. To install the project, open the Terminal and enter these commands one after the other:
      1. `brew install coreutils curl git`
      1. `brew install asdf`
      1. `git clone https://github.com/Plexlogic/dspy-intro.git`
      1. `cd dspy-intro`
      1. `asdf install`
      1. `poetry install`
   1. To open the project, enter this Terminal command (start here if you've already installed it before)
      1. `cd ~/dspy-intro`
   1. To run the project, enter this Terminal command (start here if you've already opened it - you can run it multiple times). Note you need to update it to use *your* secret key.
      1. `OPENAI_API_KEY='sk-proj-ExampleKeyExampleKeyExampleKeyExampleKeyExampleK' python dspy_intro/hello_world.py`

You can experiment by editing hello_world.py, which can be found in **dspy-intro** → **dspy_intro** in your home folder (right click Finder and click your name). For example, if you replace all the places it says `welcome_greeting` with `compliment` and run the project, it should compliment you instead.
