from openai import AsyncOpenAI
import asyncio
from datetime import datetime

api_key = os.getenv("OPENAI_API_KEY")
client = AsyncOpenAI(api_key=api_key)


def chat_streaming(prompt, context):
    # Construct the system prompt with context
    system_prompt = f"""
    You are an assistant trained to answer questions based on the following context:

    <context>
    {context}
    </context>

    Please respond clearly and accurately based on the context above.
    """

    # Make the API call with streaming enabled
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        stream=True,  # Enable streaming
    )

    # Print each token as it's received
    print("AI Response:")
    for chunk in response:
        print(chunk.choices[0].delta.get("content", ""), end="", flush=True)
    print("\n")  # Add a newline after the response


def main():
    with open("train.text", "r") as file:
        context = file.read()

    print("Welcome to the Stereo-seq X AI virtual assistant! Type 'exit' to quit.")
    while True:
        user_input = input("> ")  # Get user input
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        chat_streaming(user_input, context)

if __name__ == "__main__":
    main()
