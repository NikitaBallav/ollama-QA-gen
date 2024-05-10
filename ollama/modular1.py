import requests
import json
from pypdf import PdfReader 
import spacy
from langchain.text_splitter import SpacyTextSplitter
import csv

def generate_question_answer_pairs_from_pdf(pdf_path, model_name, prompt, output_csv):
    extracted_text = extract_text_from_pdf(pdf_path)
    all_different_chunks = split_text_into_chunks(extracted_text)
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        for i, chunk_list in enumerate(all_different_chunks):
            for j, chunk in enumerate(chunk_list):
                QA_pairs = generate_question_answer_pairs_with_ollama(model_name, prompt, chunk)
                rows = [line.split(" , ", 1) if line else ["", ""] for line in QA_pairs.split("\n")]
                csv_writer.writerow([f"List{i+1}", f"Chunk{j+1}", chunk, rows])


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
    
    chunk_size = 2000
    chunks = []
    all_different_chunks = []
    while chunk_size >= 500:
        text_splitter = SpacyTextSplitter(chunk_size=chunk_size, chunk_overlap=10)
        chunks = text_splitter.split_text(text)
        if len(chunks) > 1:
            print("Appending following chunk to the list of chunks : \n" + str(chunks) )
            all_different_chunks.append(chunks)
        #break
        chunk_size -= 100
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
        actual_response=data['response']
        return actual_response
    else:
        print("Error:", response.status_code, response.text)
        return None

# Example usage:
pdf_path = 'MLRC_english.pdf'
model_name = 'llama3'
prompt = "Frame all possible question answer pairs for the given content which is small chunk of government document, return the question answer pairs in comma separated values i.e csv format, each pair should be in new line, make sure the answers are in complete statements corresponding to each questions. The content is as follows: \n"
output_csv = 'question_answer_pairs.csv'
generate_question_answer_pairs_from_pdf(pdf_path, model_name, prompt, output_csv)