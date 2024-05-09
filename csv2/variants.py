import pandas as pd
import random

# Load the original CSV file into a pandas DataFrame
df = pd.read_csv('nlu.csv')

# Function to generate alternate question variants
def generate_variants(question):
    variants = []
    # You can modify the following lines to generate different variants based on your requirements
    variants.append(question.replace('What', 'How'))
    variants.append(question.replace('What', 'Can you tell me'))
    variants.append(question.replace('What', 'Can you describe'))
    variants.append(question.replace('What', 'Can you provide'))
    variants.append(question.replace('What', 'What is'))
    variants.append(question.replace('What', 'What are'))
    variants.append(question.replace('What', 'What are the'))
    variants.append(question.replace('What', 'What is the'))
    variants.append(question.replace('What', 'What do you know about'))
    variants.append(question.replace('What', 'What can you say about'))
    # Shuffle the list to ensure randomness
    random.shuffle(variants)
    return variants

# Create a new DataFrame to store the alternate question variants
new_rows = []
for index, row in df.iterrows():
    intent = row['intent']
    question = row['question']
    variants = generate_variants(question)
    new_rows.append({'intent': intent, 'question': question})  # Add the original question with the same intent
    for variant in variants:
        new_rows.append({'intent': intent, 'question': variant})

new_df = pd.DataFrame(new_rows)

# Save the new DataFrame with alternate question variants to a new CSV file
new_df.to_csv('new_file.csv', index=False)