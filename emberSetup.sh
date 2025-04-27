#!/bin/bash

# Update and upgrade the system
# get the Google API key and store it in a s a permanent system variable
echo "Please enter your Google API key:"
read -r google_api_key
echo "export GOOGLE_API_KEY=$google_api_key" >> ~/.bashrc
source ~/.bashrc
# Get the Ngrok API key and store it as a permanent system variable
echo "Please enter your Ngrok API key:"
read -r ngrok_api_key
echo "export NGROK_API_KEY=$ngrok_api_key" >> ~/.bashrc
source ~/.bashrc

echo "Updating and upgrading the system..."
sudo apt-get update -y && sudo apt-get upgrade -y

echo "System update and upgrade complete."

# Install Node.js and npm
echo "Installing Node.js and npm..."
curl -sL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs
echo "Node.js and npm installation complete."

python -m venv .env
source .env/bin/activate


pip install -r requirements.txt

curl -sSL https://ngrok-agent.s3.amazonaws.com/ngrok.asc \
  | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null \
  && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" \
  | sudo tee /etc/apt/sources.list.d/ngrok.list \
  && sudo apt update \
  && sudo apt install ngrok

  ngrok config add-authtoken $NGROK_API_KEY


