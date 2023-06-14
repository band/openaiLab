import chainlit as cl

@cl.on_message
async def main(message: str):
    # custom logic here

    # respond to the user
    await cl.Message(
        content=f"Received: {message}",
    ).send()

