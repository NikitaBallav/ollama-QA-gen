## Installation:

Install Ollama from its official website, with this ollama installation we can load the large language model with ease locally. 

# The following command will load the required llm:

ollama pull llama3

# After loading the llm we can chat with the llm locally, using the below command in the terminal:

ollama run llama3

# To run the ollama server, use the below command in the terminal:

ollama serve



To install the necessary components for LlamaIndex, you can use the following commands:

pip install llama-index
pip install llama-index-llms-ollama
pip install llama-index-embeddings-huggingface
pip install llama-index-readers-file

# First run the ollama server with the command 'ollama serve'
# Then run the storing_vector.py file : loading the data from the webpages and storing the corresponding embeddings
# Finally, run the chat_engine.py 
