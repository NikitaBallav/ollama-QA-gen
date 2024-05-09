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

# Initialize chunk_size
chunk_size = 1000

# Split the extracted text with decreasing chunk sizes
while chunk_size >= 100:
    # Split the text with the current chunk size
    text_splitter = SpacyTextSplitter(chunk_size=chunk_size,chunk_overlap=10)
    doc = text_splitter.split_text(extracted_text)
    
    # Print the first 20 chunks
    print(doc[:20])

    # Print the type of the doc variable
    print("Type of doc:", type(doc))

    # Print the number of chunks
    print("Number of chunks:", len(doc))

    # Decrease the chunk_size for the next iteration
    chunk_size -= 100
