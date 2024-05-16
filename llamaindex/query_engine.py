# cd /opt/conda/envs/llama_gs
#  ./bin/pip  install llama-index-llms-ollama
#  /opt/conda/envs/llama_gs/bin/pip install llama-index-embeddings-huggingface
# pip install llama-index-readers-file


# source activate /opt/conda/envs/llama_gs
# /opt/conda/envs/llama_gs/bin/python


from llama_index.core import SimpleDirectoryReader
from llama_index.llms.ollama import Ollama
llm = Ollama(model = "llama3" , request_timeout=150.0)

# documents = SimpleDirectoryReader('C:\\Users\\Nikita Ballav\\Documents\\GitHub\\ollama-QA-gen\\ollama\\pdf').load_data()
# print(documents)

from llama_index.readers.web import SimpleWebPageReader

documents = SimpleWebPageReader().load_data(
    ["https://maharashtra.nic.in/", "https://maharashtra.nic.in/infrastructure/", "https://maharashtra.nic.in/services/", "https://servicedesk.nic.in/"]
)
print(documents[0])

from llama_index.core import VectorStoreIndex
from llama_index.core import ServiceContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding


embed_model = HuggingFaceEmbedding(model_name="Alibaba-NLP/gte-large-en-v1.5", trust_remote_code=True)

service_context = ServiceContext.from_defaults(llm=llm,embed_model=embed_model)
index = VectorStoreIndex.from_documents(documents,service_context=service_context)
query_engine = index.as_query_engine()


response1 = query_engine.query("What are the services offered under NIC?")
print("response1: ",response1)

response2 = query_engine.query("Can you direct me to the service desk of NIC?")
print("response2: ",response2)

response3 = query_engine.query("Tell me about Application security?")
print("response3: ",response3)

