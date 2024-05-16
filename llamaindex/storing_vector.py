from llama_index.core import VectorStoreIndex
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings
from llama_index.readers.web import SimpleWebPageReader
from llama_index.core.node_parser import SimpleFileNodeParser



Settings.llm = Ollama(model="llama3", request_timeout=150.0)

Settings.embed_model = HuggingFaceEmbedding(model_name="Alibaba-NLP/gte-large-en-v1.5", trust_remote_code=True)

# documents = SimpleDirectoryReader(input_dir="C:\\Users\\Nikita Ballav\\Documents\\GitHub\\ollama-QA-gen\\llamaindex\\pdf").load_data()
documents = SimpleWebPageReader().load_data(
    ["https://maharashtra.nic.in/", 
     "https://maharashtra.nic.in/profile/", 
     "https://maharashtra.nic.in/publication/presentation-of-state-centre/", 
     "https://maharashtra.nic.in/directory/", 
     "https://maharashtra.nic.in/rti/",
     "https://maharashtra.nic.in/news-update/",
     "https://maharashtra.nic.in/events/",
     "https://maharashtra.nic.in/awards/",
     "https://maharashtra.nic.in/photo-gallery/",
     "https://www.nic.in/servicecontents/nicnet/",
     "https://www.nic.in/servicecontents/data-centre/",
     "https://www.nic.in/servicecontents/national-cloud/",
     "https://www.nic.in/servicecontents/messaging/",
     "https://www.nic.in/servicecontents/remote-sensing-gis/",
     "https://www.nic.in/servicecontents/webcast/",
     "https://www.nic.in/servicecontents/domain-registration/",
     "https://www.nic.in/servicecontents/nkn/",
     "https://www.nic.in/servicecontents/command-and-control-centre/",
     "https://www.nic.in/servicecontents/government-local-area-networks-lans/",
     "https://www.nic.in/servicecontents/video-conferencing/",
     "https://www.nic.in/servicecontents/security/",
     "https://www.nic.in/servicecontents/centralised-aadhaar-vault/",
     "https://maharashtra.nic.in/infrastructure/", 
     "https://maharashtra.nic.in/services/", 
     "https://servicedesk.nic.in/"]
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
index.set_index_id("vector_index2")
index.storage_context.persist("./storage2")
print("indexes are stored in a disk.")



