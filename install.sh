#!/bin/bash

# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
(echo; echo 'eval "$(/usr/local/bin/brew shellenv)"') >> ~/.zprofile
eval "$(/usr/local/bin/brew shellenv)"

# Install asdf and dependencies
brew install coreutils curl git
brew install asdf
echo '. /usr/local/opt/asdf/libexec/asdf.sh' | cat > ~/.zshrc
source ~/.zshrc

# Install asdf plugins
asdf plugin add python
asdf plugin add poetry

# Install Python and dependencies
asdf install python
asdf install poetry
poetry install
source ~/.zshrc

# Store secret key (trimming whitespace)
echo "Please enter your Open AI secret key:"
read open_ai_secret_key
open_ai_secret_key=$(echo "open_ai_secret_key" | sed 's/^[ \t]*//;s/[ \t]*$//')
echo "OPENAI_API_KEY=$open_ai_secret_key" > .env
unset open_ai_secret_key
