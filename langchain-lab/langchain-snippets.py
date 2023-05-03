
# specify the llm model
from langchain.llms import OpenAI
llm=OpenAI(model_name="text-ada-001", temperature=0))

# Alternatively, open-source LLM hosted on Hugging Face
# pip install huggingface_hub
from langchain import HuggingFaceHub
llm = HuggingFaceHub(repo_id = "google/flan-t5-xl")


# specify the document loader
from langchain.document_loaders import DirectoryLoader
loader=DirectoryLoader('/Users/band/tmp/workbench/testdir', glob="**/*.txt")

# build an index
from langchain.indexes import VectorstoreIndexCreator
index = VectorstoreIndexCreator().from_loaders([loader])

# get token estimate
# pip install tiktoken
llm.get_num_tokens("prompt? or any? string here")
