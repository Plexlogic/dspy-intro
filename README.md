# An Introduction to DSPy

## What's this?

This is a project for using [DSPy](https://github.com/stanfordnlp/dspy), a technology that writes prompts for LLMs like ChatGPT so you don't even have to do that. You simply tell it what you're giving it, and what you want it to give back.

This project shows you how to make a program which asks for the user's name and creates a greeting for them ("Hello, Plexus!"). You can easily change it to do something else, like ask the user's date of birth and give them a horoscope. Or ask for information about a prospective client and give you a BANT score if you're on the sales team. Or whatever.

## How does it work?

If you'd like to become an *engineeer* and start experimenting with AI, you will need to:

1. Ask Christian for an invite to our Open AI account so you can log in
1. Log in to Open AI and go to your secret keys at https://platform.openai.com/api-keys

   _Note once you log in you can also experiment with ChatGPT 4 at https://platform.openai.com/playground/chat (you'll need to select it under **Model**)_
1. Click **Create new secret key**, give it a name, and write it down. It will look something like this:

   `sk-proj-ExampleKeyExampleKeyExampleKeyExampleKeyExampleK`.

   ⚠️ _You secret keys are like passwords, and should never be shared (especially online)._
1. Time for some engineering (this will work on Mac only).
   1. Open the Terminal by opening the Launchpad (pictured), typing "Terminal", and clicking it
      
      ![image](https://github.com/Plexlogic/dspy-intro/assets/61395658/3b31a3d7-f629-4426-8b2d-1790e8e25a3d)
   1. Install the project by entering these commands in the Terminal one after the other:
      1. `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` (this may prompt you for your password) 
      1. `brew install coreutils curl git` (to install some things)
      1. `brew install asdf` (to install more things)
      1. `git clone https://github.com/Plexlogic/dspy-intro.git` (to download this project)
      1. `cd dspy-intro` (to go into this project)
      1. `asdf install` (to install things needed by the project)
      1. `poetry install` (to install more things needed by the project)
   1. Open the project by entering this command in the Terminal (start here if you've installed it before)

      `cd ~/dspy-intro`
   1. Run the project by entering this command in the Terminal (you can do this multiple times). Note you need to update it to use *your* secret key.

      `OPENAI_API_KEY='sk-proj-ExampleKeyExampleKeyExampleKeyExampleKeyExampleK' python dspy_intro/hello_world.py`

You can experiment by editing **hello_world.py**, which can be found in **dspy-intro** → **dspy_intro** in your home folder (right click Finder and click your name as pictured below). For example, if you replace all the places it says `welcome_greeting` with `compliment` and run the project, it should compliment you instead.

![image](https://github.com/Plexlogic/dspy-intro/assets/61395658/48ecddcd-b51f-4a35-8213-5db2f810ab22)

