import os
import openai
from InquirerPy import inquirer
from InquirerPy.base.control import Choice

API_KEY = os.getenv("API_KEY")


def select_model() -> str:
    model = inquirer.select(
        message="Please select a language model",
        choices=[
            Choice(
                name="LLaMA-3.1 Chat (8B)",
                value="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
            ),
            Choice(name="GPT-3.5 Turbo", value="gpt-3.5-turbo"),
        ],
        amark="✔️",
    ).execute()
    return model


def get_system_content() -> str:
    with open("./system_content.txt") as f:
        system_content = f.read()
    return system_content


def get_user_content():
    while True:
        try:
            result = inquirer.text(
                message="Enter email contents below:",
                multiline=True,
                validate=lambda msg: len(msg.rstrip()) > 0,
                invalid_message="Input cannot be empty",
            ).execute()
            return result
        except EOFError:
            continue


def main():
    model = select_model()
    system_content = get_system_content()
    user_content = get_user_content()
    try:
        client = openai.OpenAI(
            api_key=API_KEY,
            base_url="https://api.aimlapi.com/v1",
        )
        chat_completion = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content},
            ],
            temperature=0.2,
            max_tokens=128,
        )
        response = chat_completion.choices[0].message.content
        print("Data:\n", response)
    except openai.RateLimitError:
        print("Sorry. API rate limit exceeded, please try again later.")


if __name__ == "__main__":
    main()
