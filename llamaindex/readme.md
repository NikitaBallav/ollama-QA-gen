## Installation:

## Install Ollama from its official website, with this ollama installation we can load the large language model with ease locally. 

## The following command will load the required llm from ollama:

### ollama pull llama3

## After loading the llm we can chat with the llm locally, using the below command in the terminal:

### ollama run llama3

## To run the ollama server, use the below command in the terminal:

### ollama serve

## Install the following necessary components for LlamaIndex integrated with ollama and huggingface:

### pip install llama-index
### pip install llama-index-llms-ollama
### pip install llama-index-embeddings-huggingface
### pip install llama-index-readers-file

# 1. First run the ollama server with the command 'ollama serve'
# 2. Then run the storing_vector.py file from llamaindex folder: this will load the data from the webpages and will store the corresponding embeddings locally.
# 3. Finally, run the chat_engine.py from the same folder.
