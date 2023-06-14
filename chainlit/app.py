import openai
import chainlit as cl

#openai.api_key = "{Your_API_Key}"

model_name = "gpt-3.5-turbo"


@cl.on_chat_start
def start_chat():
    cl.user_session.set(
        "message_history",
        [{"role": "system", "content": "You are a helpful assistant."}],
    )


@cl.on_message
def main(message: str):
    message_history = cl.user_session.get("message_history")
    message_history.append({"role": "user", "content": message})

    completion = openai.ChatCompletion.create(
        model=model_name, messages=message_history
    )

    msg = cl.Message(content="")
    msg.stream_token(completion.choices[0].message.content)

    message_history.append({"role": "assistant", "content": msg.content})
    msg.send()

