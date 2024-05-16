#  Installations:
# !pip install llama-index
# !pip install llama-index-embeddings-huggingface
# !pip install llama-index-readers-file
# %pip install llama-index-embeddings-instructor

# importing libraries
from llama_index.core import SimpleDirectoryReader
import tiktoken
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.node_parser import SemanticSplitterNodeParser
from llama_index.core import VectorStoreIndex
from llama_index.core.retrievers import SummaryIndexLLMRetriever
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.llms.ollama import Ollama

# Loading Data (pdfs)
documents = SimpleDirectoryReader('C:\\Users\\Nikita Ballav\\Documents\\GitHub\\ollama-QA-gen\\llamaindex\\pdf').load_data()
print(documents)
print(f"Loaded {len(documents)} docs")

# Embeddings
embed_model = HuggingFaceEmbedding(model_name="Alibaba-NLP/gte-large-en-v1.5", trust_remote_code=True)

# Parsing (Semantic Chunker)
splitter = SemanticSplitterNodeParser(
    buffer_size=1, breakpoint_percentile_threshold=95, embed_model=embed_model
)
# the SemanticSplitterNodeParser is configured to split text into smaller chunks based on semantic similarity. It uses a buffer size of 1 to manage memory usage, a breakpoint percentile threshold of 95% to identify the most dissimilar nodes as breakpoints, and an embedding model specified by the embed_model variable to calculate the semantic similarity between nodes.
nodes = splitter.get_nodes_from_documents(documents)
print(nodes[1].get_content())

# Indexing for retriever
# 1. vector store index
# with documents
# index = VectorStoreIndex.from_documents(documents)
#  with nodes
index = VectorStoreIndex(nodes) 
# 2. Summary index
# 3. Tree index
# 4. keyword table index



# Chat engine - context mode
memory = ChatMemoryBuffer.from_defaults(token_limit=1500)

chat_engine = index.as_chat_engine(
    chat_mode="context",
    memory=memory,
    system_prompt=(
        "You are a chatbot hosted in a government website, able to have normal interactions, as well as talk about any government act, regulations, documents, code, schemes, etc."
    ),
)


# llm = Ollama(model = "llama3" , request_timeout=500.0)
# chat_engine = index.as_chat_engine(chat_mode="context", llm=llm)

response = chat_engine.chat("hello")