import requests
import json
from pypdf import PdfReader 
import spacy
from langchain.text_splitter import SpacyTextSplitter

def generate_questions_from_pdf(pdf_path, model_name, prompt):
    extracted_text = extract_text_from_pdf(pdf_path)
    chunks = split_text_into_chunks(extracted_text)
    questions = []
    for chunk in chunks:
        question = generate_question_with_ollama(model_name, prompt, chunk)
        questions.append(question)
    return questions

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    extracted_text = ""
    for page in reader.pages:
        extracted_text += page.extract_text()
    return extracted_text

def split_text_into_chunks(text):
    nlp = spacy.load("en_core_web_sm")
    total_characters = len(text)
    total_tokens = len(list(nlp(text)))
    print(f"Total characters: {total_characters}")
    print("Total number of tokens:", total_tokens)
    
    chunk_size = 20000
    chunks = []
    while chunk_size >= 10000:
        text_splitter = SpacyTextSplitter(chunk_size=chunk_size, chunk_overlap=10)
        chunks = text_splitter.split_text(text)
        if len(chunks) > 1:
            break
        chunk_size -= 10000
    return chunks

def generate_question_with_ollama(model_name, prompt, text):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-type": "application/json"}
    data = {"model": model_name, "prompt": prompt, "stream": False}
    data["prompt"] = prompt + " " + text
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data['response']
        return actual_response
    else:
        print("Error:", response.status_code, response.text)
        return None

# Example usage:
pdf_path = 'MLRC_english.pdf'
model_name = 'llama3'
prompt = 'frame all possible question answer pairs from the following content:'
# text="Sections 41 to 54 of the Maharashtra Land Revenue Code, 1966 (Mah. XLI of 1966) provide for the regulation of use of lands. Section 42 of the said Code provides for permission of the Collector for non-agricultural use of lands."
questions = generate_questions_from_pdf(pdf_path, model_name, prompt)
for i, question in enumerate(questions):
    print(f"Question {i+1}: {question}")
