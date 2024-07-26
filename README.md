# Email Parsing Using LLMs

## Description

This project employs LLMs to parse emails and obtain the sender's signature in
JSON format. Two models were compared: **LLaMA-3.1 Chat (8B)** and **GPT-3.5 Turbo** and
the findings summarised in [prompts.md](./prompts.md).

Custom instructions (the main prompt) are defined in [system_content.txt](./system_content.txt). The
emails to be parsed are provided as user input while running the application.

Three prompt iterations were done, and **GPT-3.5 Turbo** showed the most desirable
results for each iteration.

## Usage

Clone this repository and run the following commands in a unix shell (or Git Bash in Windows):

```sh
pip install -r requirements.txt
API_KEY="****" python email_parser.py
```

API_KEY refers to an API key you can obtain from <https://aimlapi.com>. You may
set it as a system environment variable or provide it when running the script as
shown above.
