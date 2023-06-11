#! /usr/bin/env python
"""
2023-06-04: code based on this Medium post:
<https://levelup.gitconnected.com/free-open-source-alternative-to-chatgpt-gpt4all-ad5828e4dcae>

2023-06-11
- seems to require two pip installs: gpt4all, gradio (these two modules bring in many more)
- this code uses a smaller model than specified in the Medium post (to work well on my PC)
  (and the model will be downloaded if not previously installed.
     this *may* require the use of a HUGGINGFACE_API_TOKEN)
- added a way to terminate (without grace) the gradio interface

"""
from gpt4all import GPT4All
gpt = GPT4All("ggml-gpt4all-j-v1.3-groovy.bin")

import gradio as gr
import os

messages = []

def main():
    
    with gr.Blocks() as mychatbot:  # Blocks is a low-level API that allows 
    # you to create custom web applications
        chatbot = gr.Chatbot()      # displays a chatbot
        question = gr.Textbox()     # for user to ask a question
        clear = gr.Button("Clear Conversation")  # Clear button
        close = gr.Button("Close Chatbot (no questions asked)")

        def close_chatbot():
            os._exit(1)
        
        # function to clear the conversation
        def clear_messages():
            global messages
            messages = []    # reset the messages list
        
        def chat(message, chat_history):
            global messages
            messages.append({"role": "user", "content": message})
            response = gpt.chat_completion(messages)
            content = response['choices'][0]['message']['content']
            messages.append({"role":"assistant", "content": content})
        
            chat_history.append((message, content))
            return "", chat_history

        # wire up the event handler for Submit button (when user press Enter)
        question.submit(fn = chat, 
                        inputs = [question, chatbot], 
                        outputs = [question, chatbot])

        # wire up the event handler for the Clear Conversation button
        clear.click(fn = clear_messages, 
                    inputs = None, 
                    outputs = chatbot, 
                    queue = False)
        
        # terminate the interface; probably not the best way to do this
        close.click(fn = close_chatbot, inputs=None, outputs=None)

    mychatbot.launch()

if __name__ == "__main__":
    exit(main())
