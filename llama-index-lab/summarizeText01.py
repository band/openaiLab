#! /usr/bin/env python
"""
This program constructs a List index of a collection of documents, and solicits summarization queries over that index.
The program is terminated by entering "quit", "exit", or "bye" at the query prompt.

code derived from <https://gpt-index.readthedocs.io/en/latest/how_to/customization/custom_llms.html> and
https://gpt-index.readthedocs.io/en/latest/use_cases/queries.html>

Required library: This command is one way to install LlamaIndex and OpenAI Python libraries.

!pip install llama-index

program assumptions:
(1) OPENAI_API_KEY or API keys for another model source is set in the shell environment
(2) documents are read from an Obsidian vault or a folder of mostly text or Markdown files
(3) GPT-index is generated every time the program is run (running cost factor)
(4) generated index is saved as `index.json`, but it is not reused

TODOs:
- save and re-use GPT-index file from previous run (save some time and money)
- maybe save queries and responses to a log file

"""

# set up logging
import logging, sys
# logging.basicConfig(level=os.environ.get('LOGLEVEL', 'WARNING').upper())
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# set up argparse
import argparse
def init_argparse():
    parser = argparse.ArgumentParser(description='Generate summarization AI from a folder of text and Markdown files.')
    parser.add_argument('--model', '-m', required=False, help='llm model_name')
    parser.add_argument('--directory', '-d', required=True, help='directory of text and Markdown files')
    return parser

# import LLM modules
from llama_index import LLMPredictor, PromptHelper, ServiceContext, StorageContext
from llama_index import SimpleDirectoryReader, ObsidianReader
from llama_index import GPTListIndex

from langchain import OpenAI

def main():
    argparser = init_argparse();
    args = argparser.parse_args();
    logging.debug(f"args: {args}")

    file_dir = str(args.directory)
    logging.info("files directory: %s", file_dir)

    # define LLM
    # use 'text-ada-001' if no model_name provided
    llm_model_name = "text-ada-001"
    if args.model:
        llm_model_name = str(args.model)

    logging.info("llm model name: %s", llm_model_name)
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name=llm_model_name))
    
    # define prompt helper
    max_input_size = 4096
    num_output = 256
    max_chunk_overlap = 20
    # note: it is odd (to me) that PromptHelper expects these 3 args in this order; why are they not assigned?
    prompt_helper = PromptHelper(max_input_size, num_output, max_chunk_overlap)

    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)

    storage_context = StorageContext.from_defaults()
    
    # Loading documents 
    print("Loading docs from ", file_dir)
    documents = ObsidianReader(file_dir).load_data() # Returns list of Documents

    # Construct a simple vector index
    index = GPTListIndex.from_documents(
        documents, service_context=service_context
    )

    # Save your index to a ./storage directory
    index.storage_context.persist()
    # Load the saved index TODO: this needs more context and code
    
    # Query the index
    query_engine = index.as_query_engine(response_mode="tree_summarize")
    while True:
        # run a query read from the input
        query = input("enter a query: ")
        match query.split():
            case ["quit" | "-q" | "exit" | "bye"]:
                logging.debug("we quit!")
                quit()
            case _:
                print(f"run this query: {query!r} ")
                response = query_engine.query(f"{query!r}")
                print(response)
 
if __name__ == "__main__":
    exit(main())

