#level 2 task 5 a word occurrence counter
import re
from collections import Counter
import os

def count_word_occurrences(file_name):
    # fetch the file path 
    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), file_name)

    # Read the content of the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Remove  non alphabetical characters and convert to lowercase
    words = re.findall(r'\b\w+\b', content.lower())

    # Count occurrences 
    word_counts = Counter(words)

    # Display results in alphabetical order
    sorted_word_counts = sorted(word_counts.items())

    # Print the results
    for word, count in sorted_word_counts:
        print(f'{word}: {count}')

# Use the function with the file name directly
count_word_occurrences('words.txt')
