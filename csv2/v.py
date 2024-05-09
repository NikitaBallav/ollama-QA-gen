import csv
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from random import shuffle

# Function to generate alternate variants for a given question
def generate_alternate_variants(question):
    tokens = word_tokenize(question)
    alternate_variants = []

    for token in tokens:
        synonyms = set()
        antonyms = set()

        for syn in wordnet.synsets(token):
            for lemma in syn.lemmas():
                synonyms.add(lemma.name().replace('_', ' '))
                if lemma.antonyms():
                    antonyms.add(lemma.antonyms()[0].name().replace('_', ' '))

        # Add synonyms and antonyms to alternate variants
        if synonyms:
            alternate_variants.extend([' '.join(tokens[:tokens.index(token)] + [syn] + tokens[tokens.index(token)+1:]) for syn in synonyms])
        if antonyms:
            alternate_variants.extend([' '.join(tokens[:tokens.index(token)] + [ant] + tokens[tokens.index(token)+1:]) for ant in antonyms])

    shuffle(alternate_variants)
    return alternate_variants[:10] if len(alternate_variants) >= 10 else alternate_variants

# Function to read intents and questions from CSV file and write alternate variants to a new CSV file
def generate_alternate_variants_csv(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames + ['alternate_variant_{}'.format(i) for i in range(1, 11)]
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in reader:
                question = row['question']
                alternate_variants = generate_alternate_variants(question)
                row.update({'alternate_variant_{}'.format(i+1): variant for i, variant in enumerate(alternate_variants)})
                writer.writerow(row)

# Example usage
if __name__ == "__main__":
    input_file = 'nlu.csv'  # Replace with your input CSV file
    output_file = 'alternate_variants.csv'  # Replace with the desired output CSV file
    generate_alternate_variants_csv(input_file, output_file)
