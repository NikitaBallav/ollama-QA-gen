from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core import VectorStoreIndex
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings
from llama_index.readers.web import SimpleWebPageReader
from llama_index.core.node_parser import SimpleFileNodeParser
from llama_index.core import SimpleDirectoryReader
from llama_index.core import load_index_from_storage, StorageContext

Settings.llm = Ollama(model="llama3", request_timeout=150.0)
Settings.embed_model = HuggingFaceEmbedding(model_name="Alibaba-NLP/gte-large-en-v1.5", trust_remote_code=True)

# documents = SimpleDirectoryReader(input_dir="C:\\Users\\Nikita Ballav\\Documents\\GitHub\\ollama-QA-gen\\llamaindex\\pdf").load_data()
documents = SimpleWebPageReader().load_data(
    ["https://maharashtra.nic.in/", "https://maharashtra.nic.in/infrastructure/", "https://maharashtra.nic.in/services/", "https://servicedesk.nic.in/"]
)

print("webpages are loaded.")
# print("chunking the webpages")
# parser = SimpleFileNodeParser()
# nodes = parser.get_nodes_from_documents(documents)
# print("nodes of the webpages are successfully created.")

index = VectorStoreIndex.from_documents(documents, llm=Settings.llm, embed_model=Settings.embed_model)
# index = VectorStoreIndex(nodes, llm=Settings.llm, embed_model=Settings.embed_model)

print("vector indexing is set")

# save index to disk
index.set_index_id("vector_index3")
index.storage_context.persist("./storage3")
print("indexes are stored in a disk.")

storage_context = StorageContext.from_defaults(persist_dir="storage3")
# load index from the disk
index = load_index_from_storage(storage_context, index_id="vector_index3")


memory = ChatMemoryBuffer.from_defaults(token_limit=8192) 
chat_engine = index.as_chat_engine(
    chat_mode="context",
    system_prompt="You are a helpful AI assistant.",
    memory=memory
)
print("running chat_engine.")
chat_engine.chat_repl()



