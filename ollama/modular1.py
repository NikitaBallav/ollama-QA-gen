import requests
import json
from pypdf import PdfReader 
import spacy
from langchain.text_splitter import SpacyTextSplitter

def generate_question_answer_pairs_from_pdf(pdf_path, model_name, prompt):
    extracted_text = extract_text_from_pdf(pdf_path)
    chunks = split_text_into_chunks(extracted_text)
    pairs = []
    for chunk in chunks:
        chunk_pairs = generate_question_answer_pairs_with_ollama(model_name, prompt, chunk)
        pairs.extend(chunk_pairs)
    return pairs

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
    all_different_chunks = []
    while chunk_size >= 10000:
        text_splitter = SpacyTextSplitter(chunk_size=chunk_size, chunk_overlap=10)
        chunks = text_splitter.split_text(text)
        if len(chunks) > 1:
            print("Appending following chunk to the list of chunks : \n" + str(chunks) )
            all_different_chunks.append(chunks)
        #break
        chunk_size -= 1000
    print("All different chunks are as following " + str(all_different_chunks))
    return all_different_chunks

def generate_question_answer_pairs_with_ollama(model_name, prompt, text):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-type": "application/json"}
    data = {"model": model_name, "prompt": prompt, "stream": False}
    data["prompt"] = prompt + " " + text
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        pairs = []
        for item in data['response'].split("\n"):
            if item.strip() != "":
                question, answer = item.split("|")
                pairs.append((question.strip(), answer.strip()))
        return pairs
    else:
        print("Error:", response.status_code, response.text)
        return None

# Example usage:
pdf_path = 'MLRC_english.pdf'
model_name = 'llama3'
prompt = "Your objective is to develop a robust question-and-answer database to train a chatbot for government website. Create question-answer pairs that enable users to obtain information about any government documentation. Ensure that no important information is overlooked. Frame all possible question-answer pairs from the following chunk:\n"
pairs = generate_question_answer_pairs_from_pdf(pdf_path, model_name, prompt)
for i, pair in enumerate(pairs):
    print(f"Pair {i+1}: Question - {pair[0]}, Answer - {pair[1]}")
