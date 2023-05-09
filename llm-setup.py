
# get config info from llama.yaml file (2023-05-06)
import yaml
with open('./llama.yaml') as file:
    config = yaml.safe_load(file)

if 'llm_model_name' in config:
    llm_model_name = config.get('llm_model_name')

if 'index_storage_dir' in config:
    index_storage_dir = config['index_storage_dir']

