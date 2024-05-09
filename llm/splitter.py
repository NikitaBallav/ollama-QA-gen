# importing required classes 
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

chunk_size = 20000
chunks = []
all_different_chunks = []
while chunk_size >= 10000:
    text_splitter = SpacyTextSplitter(chunk_size=chunk_size, chunk_overlap=10)
    chunks = text_splitter.split_text(extracted_text)
    if len(chunks) > 1:
        print("Appending following chunk to the list of chunks : \n" + str(chunks) )
        all_different_chunks.append(chunks)
        #break
    chunk_size -= 1000
print("All different chunks are as following " + str(all_different_chunks))
#return all_different_chunks

# # Initialize chunk_size
# chunk_size = 2000

# # Split the extracted text with decreasing chunk sizes
# while chunk_size >= 1000:
#     # Split the text with the current chunk size
#     text_splitter = SpacyTextSplitter(chunk_size=chunk_size,chunk_overlap=10)
#     doc = text_splitter.split_text(extracted_text)
    
#     # Print the first 20 chunks
#     print(doc[:20])

#     # Print the type of the doc variable
#     print("Type of doc:", type(doc))

#     # Print the number of chunks
#     print("Number of chunks:", len(doc))

#     # Decrease the chunk_size for the next iteration
#     chunk_size -= 1000
