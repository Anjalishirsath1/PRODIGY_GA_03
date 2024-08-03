# -*- coding: utf-8 -*-
"""Text Generation with Markov Chains

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1V2ecgOnvEmQHKv7Dcdmv2wG7fnXnxbY_
"""

pip install markovify pandas



import markovify

# Sample text data
text = """
Your sample text goes here. It can be any length and content.
Markov chains are a fascinating tool for text generation! Essentially, they model the probability of each word (or character) based on the previous ones.
Here’s a basic rundown of how they work in text generation.
"""

# Build the Markov chain model
text_model = markovify.Text(text)

# Generate a random sentence
def generate_sentence(model):
    sentence = model.make_sentence()
    if sentence:
        return sentence
    else:
        return "Unable to generate a sentence."

# Generate a longer piece of text
def generate_text(model, sentences=5):
    generated_sentences = []
    for _ in range(sentences):
        sentence = model.make_sentence()
        if sentence:  # Check if the sentence is not None
            generated_sentences.append(sentence)
        else:
            generated_sentences.append("Unable to generate a sentence.")
    return ' '.join(generated_sentences)

# Example usage
print("Random Sentence:")
print(generate_sentence(text_model))

print("\nGenerated Text:")
print(generate_text(text_model, sentences=5))

import random
from collections import defaultdict

# Sample text data
text = """
Your sample text goes here. It can be any length and content.
Markov chains are a fascinating tool for text generation! Essentially, they model the probability of each word (or character) based on the previous ones.
Here’s a basic rundown of how they work in text generation.
"""

# Tokenize the text into words
words = text.split()

# Build the Markov chain model
model = defaultdict(lambda: defaultdict(int))

for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]
    model[current_word][next_word] += 1

# Convert counts to probabilities
for current_word, next_words in model.items():
    total_count = sum(next_words.values())
    for next_word in next_words:
        next_words[next_word] /= total_count

# Generate text based on the Markov chain model
def generate_text(model, start_word, length=50):
    current_word = start_word
    output_words = [current_word]

    for _ in range(length - 1):
        next_words = model[current_word]
        if not next_words:
            break
        next_word = random.choices(list(next_words.keys()), weights=next_words.values())[0]
        output_words.append(next_word)
        current_word = next_word

    return ' '.join(output_words)

# Example usage
start_word = random.choice(words)  # Pick a random starting word
print("Generated Text:")
print(generate_text(model, start_word))

