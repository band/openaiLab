#! /usr/bin/env python3
"""
This program generates an OpenAI chat-bot from a directory of text files and reads queries from the command line.
Program is terminated by entering "quit", "exit", or "bye" at the query prompt.

code derived from <https://bootcamp.uxdesign.cc/a-step-by-step-guide-to-building-a-chatbot-based-on-your-own-documents-with-gpt-2d550534eea5>
A step-by-step guide to building a chatbot based on your own documents with GPT

Required library: This command is one way to install LlamaIndex and OpenAI Python libraries.

!pip install llama-index

program assumptions:
(1) OPENAI_API_KEY has been set in the shell environment
(2) documents are read from a directory containing only text documents
(3) GPT-index is generated every time the program is run (running cost factor)
(4) generated index is saved as `index.json`, but it is not reused

TODOs:
- save and re-use GPT-index file from previous run (save some time and money)
- maybe save queries and responses to a log file

"""

# import needed packages
from llama_index import GPTSimpleVectorIndex, Document, download_loader
import os
from pathlib import Path

# set up logging
import logging
logging.basicConfig(level=os.environ.get('LOGLEVEL', 'WARNING').upper())

# set up argparse
import argparse
def init_argparse():
    parser = argparse.ArgumentParser(description='Generate OpenAI chat-bot from a directory of text files.')
    parser.add_argument('--directory', '-d', required=True, help='directory')
    return parser

def main():
    argparser = init_argparse();
    args = argparser.parse_args();
    logging.debug(f"args: {args}")
    
    text_dir = str(args.directory)
    logging.info("text file directory: %s", text_dir)

    # Loading from a directory
    print("Loading from directory ", text_dir)
    SimpleDirectoryReader = download_loader("SimpleDirectoryReader")
    loader = SimpleDirectoryReader(text_dir, recursive=False, exclude_hidden=True)
    documents = loader.load_data() # Returns list of documents

    # Construct a simple vector index
    print(dir(GPTSimpleVectorIndex))
    index = GPTSimpleVectorIndex.from_documents(documents)

    # Save your index to a index.json file
    index.save_to_disk('index.json')
    # Load the index from your saved index.json file
#    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    
    # Query the index
    while True:
        # run a query read from the input
        query = input("$ ")
        match query.split():
            case ["quit" | "exit" | "bye"]:
                logging.debug("we quit!")
                quit()
            case _:
                print(f"run this query: {query!r}.")
                response = index.query(f"{query!r}")
                print(response)
 
if __name__ == "__main__":
    exit(main())

