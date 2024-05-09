
# # Using spacy

import spacy
from pypdf import PdfReader 
from langchain.text_splitter import SpacyTextSplitter

# creating a pdf reader object 
reader = PdfReader('MLRC_english.pdf') 
  
# initialize an empty string to store the extracted text
extracted_text = ""

# iterate through each page in the PDF
for page in reader.pages:
    # extract text from each page and concatenate it to the extracted_text string
    extracted_text += page.extract_text()
print(extracted_text)
print("extraction is complete.")


# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# extracted_text="rani is dancing, singing in the rain. Raju went to school with his dog. Mother is in the kitchen."

# Process the text with spaCy i.e. 
doc = nlp(extracted_text)

total_characters = len(extracted_text)
total_tokens = len(list(doc))

# # Get the total number of tokens excluding punctuation
# num_tokens = sum(1 for token in doc if not token.is_punct)


print(f"Total characters: {total_characters}")
print("Total number of tokens:", total_tokens)


# text_splitter = SpacyTextSplitter(chunk_size=300000, chunk_overlap=1000)
# doc = text_splitter.split_text(extracted_text)

# # Print the chunk size of each chunk
# for i, chunk in enumerate(doc):
#     # print(f"Chunk {i+1}: {chunk}")
#     print(f"Chunk {i+1} size: {len(chunk)}")
    
# # Print the type of the doc variable
# print("Type of doc:", type(doc))

# # Print the number of chunks
# print("Number of chunks:", len(doc))

# Initialize chunk_size
chunk_size = 20000

# Split the extracted text with decreasing chunk sizes
while chunk_size >= 10000:
    # Split the text with the current chunk size
    text_splitter = SpacyTextSplitter(chunk_size=chunk_size,chunk_overlap=10)
    doc = text_splitter.split_text(extracted_text)
    
    for i, chunk in enumerate(doc):
    # print(f"Chunk {i+1}: {chunk}")
        print(f"Chunk {i+1} size: {len(chunk)}")

    # Print the type of the doc variable
    print("Type of doc:", type(doc))

    # Print the number of chunks
    print("Number of chunks:", len(doc))

    # Decrease the chunk_size for the next iteration
    chunk_size -= 10000


# import spacy

# nlp = spacy.load("en_core_web_sm")
# extracted_text = "Hi, how are you? I'm good!"
# doc = nlp(extracted_text)
# total_characters = len(extracted_text)
# total_tokens = len(list(doc))
# print(doc)
# print("Tokens:", total_tokens) 
# print("Characters:", total_characters) 

