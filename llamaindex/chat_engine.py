from llama_index.core import load_index_from_storage, StorageContext
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings
from llama_index.core.memory import ChatMemoryBuffer

Settings.llm = Ollama(model="llama3", request_timeout=150.0)

Settings.embed_model = HuggingFaceEmbedding(model_name="Alibaba-NLP/gte-large-en-v1.5", trust_remote_code=True)

storage_context = StorageContext.from_defaults(persist_dir="storage")
# load index from the disk
index = load_index_from_storage(storage_context, index_id="vector_index")


memory = ChatMemoryBuffer.from_defaults(token_limit=8192) 
chat_engine = index.as_chat_engine(
    chat_mode="context",
    system_prompt="You are a helpful AI assistant to interact with humans and help them with their queries by providing accurate responses along with the source url link.",
    memory=memory
)
print("running chat_engine.")
chat_engine.chat_repl()


# response1 = chat_engine.chat("What are the services offered under NIC?")
# print(response1)

# print("--------")
# response2 = chat_engine.chat("Provide me the url or link from where I can get to know about the infrastructure of NIC?")
# print(response2)

