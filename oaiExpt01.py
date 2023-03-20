#! /usr/bin/env python
"""
This program generates an OpenAI chat-bot from an Obsidian vault and reads queries from the command line.
Program is terminated by entering "quit", "exit", or "bye" at the query prompt.

code derived from <https://bootcamp.uxdesign.cc/a-step-by-step-guide-to-building-a-chatbot-based-on-your-own-documents-with-gpt-2d550534eea5>
A step-by-step guide to building a chatbot based on your own documents with GPT

Required libraries: These commands are one way to install both LlamaIndex and OpenAI Python libraries.

!pip install llama-index
!pip install openai

program assumptions:
(1) an OPENAI_API_KEY is available in a file named 'oaikey.txt' in the current directory.
(2) documents are read from an Obsidian vault
(3) GPT-index is generated every time the program is run (running cost factor)

TODOs:
- save and re-use GPT-index file from previous run (save some time and money)
- maybe save queries and responses to a log file

"""

# import needed packages
from llama_index import GPTSimpleVectorIndex, Document, SimpleDirectoryReader
from llama_index import download_loader
import os
from pathlib import Path

# set up logging
import logging
logging.basicConfig(level=os.environ.get('LOGLEVEL', 'WARNING').upper())

# set up argparse
import argparse
def init_argparse():
    parser = argparse.ArgumentParser(description='Generate OpenAI chat-bot from an Obsidian vault Markdown pages.')
    parser.add_argument('--vault', '-v', required=True, help='directory containing Markdown files')
    return parser

# set openAI API key
os.environ['OPENAI_API_KEY'] = Path('oaikey.txt').read_text().replace('\n','')
    
def main():
    argparser = init_argparse();
    args = argparser.parse_args();
    logging.debug(f"args: {args}")
    
    vault_dir = str(args.vault)
    logging.info("vault directory: %s", vault_dir)

    # Loading from an Obsidian vault
    print("Loading from Obsidian vault ", vault_dir)
    ObsidianReader = download_loader('ObsidianReader')
    documents = ObsidianReader(vault_dir).load_data() # Returns list of documents

    # Construct a simple vector index
    index = GPTSimpleVectorIndex(documents)

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

