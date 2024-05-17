# An Introduction to DSPy

## What's this?

This is a project for using [DSPy](https://github.com/stanfordnlp/dspy), a technology that writes prompts for LLMs like ChatGPT so you don't even have to do that. You simply tell it what you're giving it, and what you want it to give back.

This project shows you how to make a program which asks for the user's name and creates a greeting for them ("Hello, Plexus!"). You can easily change it to do something else, like ask the user's date of birth and give them a horoscope. Or ask for information about a prospective client and give you a BANT score if you're on the sales team. Or whatever.

## How does it work?

If you'd like to become an *engineeer* and start experimenting with AI, you will need to follow these steps.

### Installation

First, you will need a "secret key" to use our Open AI account. Secret keys are like passwords, and should never be shared.

1. Ask Christian for an invite to our Open AI account so you can log in.
1. Log in to Open AI and go to your secret keys at https://platform.openai.com/api-keys.

   Note once you log in you can also experiment with ChatGPT 4 at https://platform.openai.com/playground/chat (you'll need to select it under **Model**).
1. Click **Create new secret key** and give it a name. It will look something like this:

   `sk-proj-ExampleKeyExampleKeyExampleKeyExampleKeyExampleK`

Now you have your secret key, you can begin the installation:

1. Install Git by downloading and running the installer at https://sourceforge.net/projects/git-osx-installer/.
1. Open Terminal by pressing ⌘ + SPACE, searching for **Terminal**, and clicking it.
1. Download the project and go into it by entering these commands (copy each into the Terminal and press ENTER):
   1. `cd ~/`
   1. `git clone https://github.com/Plexlogic/dspy-intro.git`
   1. `cd ~/dspy-intro`
1. Run the installation script:
   1. `./install.sh`
   1. You will be prompted to enter your password (for security, it will not be displayed as you type).
   1. You will be prompted to press RETURN/ENTER (there may be a long wait after this).
   1. You will be prompted to enter your Open AI secret key, which will be stored in a `.env` file.

If you ever need a new Open AI secret key, you can repeat the installation process.

### Usage

Once the project is installed (see above), it can be run with these steps:

1. If you haven't already, open Terminal as described in the installation steps.
2. Make sure you're in the project with the command `cd ~/dspy-intro`.
1. Run the project by entering this command in the Terminal. You can do this multiple times (in Terminal, you can press UP to repeat the previous command).
   
   `python dspy_intro/hello_world.py`

After running the project, you can experiment by editing **hello_world.py**, which can be found in **dspy-intro** → **dspy_intro** in your home folder (right click Finder and click your name as pictured below). For example, if you replace all the places it says `welcome_greeting` with `compliment` and run the project, it should compliment you instead.

![image](https://github.com/Plexlogic/dspy-intro/assets/61395658/48ecddcd-b51f-4a35-8213-5db2f810ab22)
