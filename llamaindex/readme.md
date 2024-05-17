## Installation:

Install Ollama from its official website, with this Ollama installation we can load the large language model with ease locally.

The following command will load the required LLM from Ollama:

```
ollama pull llama3
```

After loading the LLM, we can chat with the LLM locally, using the below command in the terminal:

```
ollama run llama3
```

To run the Ollama server, use the below command in the terminal:

```
ollama serve
```

Install the following necessary components for LlamaIndex integrated with Ollama and Hugging Face:

```
pip install llama-index
pip install llama-index-llms-ollama
pip install llama-index-embeddings-huggingface
pip install llama-index-readers-file
pip install llama-index-readers-web

```

1. First run the Ollama server with the command `ollama serve`
2. Then run the `storing_vector.py` file from the LlamaIndex folder: this will load the data from the webpages and will store the corresponding embeddings locally.
3. Finally, run the `chat_engine.py` from the same folder
