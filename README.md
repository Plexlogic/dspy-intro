# An Introduction to DSPy

## What's this?

This is a project for using [DSPy](https://github.com/stanfordnlp/dspy), a technology that writes prompts for LLMs like ChatGPT so you don't even have to do that. You simply tell it what you're giving it, and what you want it to give back.

This project shows you how to make a program which asks for the user's name and creates a greeting for them ("Hello, Plexus!"). You can easily change it to do something else, like ask the user's date of birth and give them a horoscope. Or ask for information about a prospective client and give you a BANT score if you're on the sales team. Or whatever.

## How does it work?

If you'd like to become an *engineeer* and start experimenting with AI, you will need to follow these steps.

### Installation

First, you will need a "secret key" to use our Open AI account. Secret keys are like passwords, and should never be shared.

1. Ask Christian for an invite to our Open AI account so you can log in
1. Log in to Open AI and go to your secret keys at https://platform.openai.com/api-keys

   Note once you log in you can also experiment with ChatGPT 4 at https://platform.openai.com/playground/chat (you'll need to select it under **Model**).
1. Click **Create new secret key**, give it a name, and record it somewhere safe. It will look something like this:

   `sk-proj-ExampleKeyExampleKeyExampleKeyExampleKeyExampleK`.

Next, it's time for some engineering. Note these installation steps will only work on Mac. Be very careful to enter all commands *exactly* - you will get errors if there are any mistakes.

1. Open Terminal by pressing ⌘ + SPACE, searching for "Terminal", and clicking it.
1. Install Homebrew, which we will use to install everything else, by entering these commands:
   1. `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
   1. You will be prompted to enter your password (for security, it will not be displayed as you type)
   1. You will be prompted to press RETURN/ENTER to continue.
   1. Installation may take a while.
   1. The Terminal will display two more commands which you will need to run, which look something like:

      `(echo; echo 'eval "$(/usr/local/bin/brew shellenv)"') >> /Users/yourename/.zprofile`

      `eval "$(/usr/local/bin/brew shellenv)"` 
1. Use Homebrew to install asdf with these commands:
   1. `brew install coreutils curl git`
   1. `brew install asdf` (installs asdf)
   1. `echo '. /usr/local/opt/asdf/libexec/asdf.sh' | cat > ~/.zshrc`
   1. Restart Terminal.
1. Setup asdf:
   1. `asdf plugin add python`
   1. `asdf plugin add poetry`
1. Download the project and go into it:
   1. `git clone https://github.com/Plexlogic/dspy-intro.git`
   1. `cd dspy-intro`
1. Install things needed by the project, with these commands:
   1. `asdf install python` (installs Python, the programming language)
   1. `asdf install poetry` (installs Poetry, which installs things used by the project)
   1. `poetry install` (installs things used by the project, DSPy)
1. Congratulations, you have used Homebrew to install asdf to install Poetry to install DSPy. This is the sort of nonsense we pay the engineering team for.

### Usage

Once the project is installed (see above), it can be run with these steps:

1. If you haven't already, open Terminal as described in the installation steps.
2. Make sure you're in the project with the command `cd ~/dspy-intro`.
1. Run the project by entering this command in the Terminal (you can do this multiple times). Note you need to update it to use *your* secret key (see installation steps to get one).
   
   `OPENAI_API_KEY='sk-proj-ExampleKeyExampleKeyExampleKeyExampleKeyExampleK' python dspy_intro/hello_world.py`

   You can run the project again by repeating this command. In Terminal, you can press the UP key to load previous commands.

After running the project, you can experiment by editing **hello_world.py**, which can be found in **dspy-intro** → **dspy_intro** in your home folder (right click Finder and click your name as pictured below). For example, if you replace all the places it says `welcome_greeting` with `compliment` and run the project, it should compliment you instead.

![image](https://github.com/Plexlogic/dspy-intro/assets/61395658/48ecddcd-b51f-4a35-8213-5db2f810ab22)
