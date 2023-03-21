# OpenAI Laboratory

- A repository to hold explorations and experiments with using OpenAI.

- We try to keep the lab bench clean, but there is no guarantee that
  what is here today will be here tomorrow.

-----

# oaiExpt01 - 

oaiExpt01 is a command-line Python script that indexes the contents of an Obsidian vault and reads queries on that index from the command line.

Comments and bug reports are welcome at <https://github.com/band/openaiLab/issues>, and I'm happy to review pull requests.

Note, there may be some breaking design or input/output method changes in future versions to support more indexing model options and run time efficiencies.

## Requirements

- Python 3.10 or higher
- `llama-index` and `openai` libraries

## Installation

1. Clone this repository or download the `oaiExpt01.py` file.
2. Install the `llama-index` and `openai` libraries (`openai` is part of the `llama-index` install)
  - (recommended: activate a Python virtual environment first):

```bash
pip install llama-index
```

## Usage

Set the OPENAI_API_KEY environment variable to your OpenAI API key:

```bash
export OPENAI_API_KEY="your_openai_api_key_here"
```

You can copy `env.sh-template` to `env.sh`, add your API key to it, and then use `source env.sh` to add your API key to the environment.

Run the program

```bash
python3 oaiExpt01.py -v /path/to/obsidian/vault
```

Or you can change directory to where `oaiExpt01.py` is located and run it as an executable:

```bash
./oaiExpt01.py -v /path/to/obsidian/vault
```

It can take some time to generate an index; be patient. Enter a query at the `$` prompt.  
To terminate the program enter "quit", "exit", or "bye" at the `$` prompt.    

## License

This project is licensed under the MIT License. See the LICENSE file for details.
