#! /usr/bin/env python3
"""
This program generates an OpenAI chat-bot from a directory and reads queries from the command line.
It uses a loader that extracts text from a variety of unstructured text files:
  <https://llamahub.ai/l/file-unstructured>
2023-04-24: N.B.: the SimpleDirectoryReader code does not work as written.

Program is terminated by entering "quit", "exit", or "bye" at the query prompt.

Required library: This command is one way to install LlamaIndex and OpenAI Python libraries.

!pip install llama-index

program assumptions:
(1) OPENAI_API_KEY has been set in the shell environment
(2) GPT index is generated every time the program is run (running cost factor)
(4) generated index is saved as `index.json`, but it is not reused

TODOs:
- save and re-use GPT index file from previous run (save some time and money)
- maybe save queries and responses to a log file

"""

import glob
from pathlib import Path

from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex, download_loader
UnstructuredReader = download_loader('UnstructuredReader')
loader = UnstructuredReader()

# set up logging
import logging, os
logging.basicConfig(level=os.environ.get('LOGLEVEL', 'WARNING').upper())

# set up argparse
import argparse
def init_argparse():
    parser = argparse.ArgumentParser(description='Generate OpenAI chat-bot from a directory of text & markdown files.')
    parser.add_argument('--directory', '-d', required=True, help='directory')
    return parser

def main():
    argparser = init_argparse();
    args = argparser.parse_args();
    logging.debug(f"args: {args}")
    
    dir_path = Path(args.directory).resolve().as_posix()
    logging.info("directory %s: ", dir_path)

    # grab some test files
    documents = []
    allfiles = [Path(f).as_posix() for f in glob.iglob(f"{dir_path}/**/*.*", recursive=True, include_hidden=False)]

    for file_path in allfiles:
        print(file_path)
        documents.extend(loader.load_data(file=file_path, split_documents=False))

    logging.debug("how many documents? ", len(documents))

    index = GPTSimpleVectorIndex.from_documents(documents)

    # Query the index
    while True:
        # run a query read from the input
        query = input("enter a query: ")
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
