# importing required classes 
from pypdf import PdfReader 
from langchain.text_splitter import SpacyTextSplitter
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain
# from langchain.chat_models import ChatOpenAI
# import os

# creating a pdf reader object 
reader = PdfReader('MLRC_english.pdf') 
  
# initialize an empty string to store the extracted text
question_gen = ""

# iterate through each page in the PDF
for page in reader.pages:
    # extract text from each page and concatenate it to the extracted_text string
    question_gen += page.extract_text()

print(question_gen)
print("extraction is complete.")

# Initialize chunk_size
chunk_size = 1000

# Split the extracted text with decreasing chunk sizes
while chunk_size >= 100:
    # Split the text with the current chunk size
    text_splitter = SpacyTextSplitter(chunk_size=chunk_size,chunk_overlap=10)
    doc = text_splitter.split_text(question_gen)
    document_ques_gen = [Document(page_content=t) for t in doc]
    
    # Print the first 20 chunks
    print(doc[:20])

    # Print the type of the doc variable
    print("Type of doc:", type(doc))

    # Print the number of chunks
    print("Number of chunks:", len(doc))

    hf = HuggingFacePipeline.from_model_id(
        model_id="",
        task="text-generation",
        pipeline_kwargs={"max_new_tokens": 10},
    )

    print("model is successfully loaded")
    
    # Creating chain

    prompt_template = """
        You are an expert at creating questions based on materials and documentation.
        Your goal is to prepare a robust Question and answer database to train a chatbot.
        You do this by asking questions about the text below:

        ------------
        {text}
        ------------

        Create questions that will help the users to gain information regarding any government act.
        Make sure not to lose any important information.

        QUESTIONS:
        """

    PROMPT_QUESTIONS = PromptTemplate(template=prompt_template, input_variables=["text"])

    refine_template = ("""
        You are an expert at creating questions based on government circulars and documentation.
        Your goal is to help a user to gain information regarding any government regulations.
        We have received some practice questions to a certain extent: {existing_answer}.
        We have the option to refine the existing questions or add new ones.
        (only if necessary) with some more context below.
        ------------
        {text}
        ------------

        Given the new context, refine the original questions in English.
        If the context is not helpful, please provide the original questions.
        QUESTIONS:
        """
        )

    REFINE_PROMPT_QUESTIONS = PromptTemplate(
            input_variables=["existing_answer", "text"],
            template=refine_template,
        )

    ques_gen_chain = load_summarize_chain(llm = llm_ques_gen_pipeline, 
                                                chain_type = "refine", 
                                                verbose = True, 
                                                question_prompt=PROMPT_QUESTIONS, 
                                                refine_prompt=REFINE_PROMPT_QUESTIONS)

    ques = ques_gen_chain.run(document_ques_gen)

    print(ques)

# Decrease the chunk_size for the next iteration
    chunk_size -= 400


