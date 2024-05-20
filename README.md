#README 
# Welcome!
Hi! GPT - 4U is a modern and security-focused interface for Large Language Models. I've included a host of features that I hope you enjoy. Feel free to use it, share it, modify it, and use it however you want (legally of course 😘). No need to attribute me or even ask for my permission. It's completely free! 

![Screenshot](./images/GPT4U-Screenshot.png)

Features:
- Pay as you use it, no need to pay an exorbitant fixed monthly fee.
- All your chat histories are stored in local text files. This means they can easily be moved, stored, or synced with your team via a plethora of cloud storage services. Think of the possibilities for team collaboration!
- Provides usage statistics.

# Installation
First set up an OpenAI API key at [OpenAI's website](https://platform.openai.com/playground).
## Docker-ized Version (Recommended for beginners)
I created a Docker image to package this application. To run the Docker Container:
1. Verify the [Docker Desktop](https://www.docker.com/products/docker-desktop/) application is installed.
2. In terminal, run the command `docker build -t gpt4u .`
3. In terminal, run the command `docker run -it -p 7860:7860 gpt4u`
4. In your browser enter the url http://0.0.0.0:7860 and hit enter.
5. The user interface will launch.

## Run Directly
1. Open the terminal to `GPT-4U`.
2. In terminal, run the command `pip install -r Requirements.txt`
3. In terminal, run the command `python3 webapp-launch.py`
4. In your browser enter the url http://0.0.0.0:7860 and hit enter.
5. The user interface will launch.

# Usage
1. Expand the *Settings* accordion.
2. Select a model from the *Model* dropdown.
3. Enter your OpenAI API key into the *OpenAI API Key* textbox.
4. Select a chat from the *Chat Selection* dropdown.
5. Input a prompt. Hit the enter key.

# Roadmap
- [ ] Advanced usage statistics.
- [ ] Custom/Local LLM support.

More Images
![Screenshot](./images/GPT-4U-Settings-Screenshot.png)
