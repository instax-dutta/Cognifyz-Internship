#task5 file manipulation 
import os
def count_word_occurrences(file_path):
    word_counts = {}

    with open(file_path, 'r') as file:
        for line in file:
            words = line.lower().split()
            for word in words:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1

    sorted_items = sorted(word_counts.items())

    for word, count in sorted_items:
        print(f"{word}: {count}")

file_path = 'words.txt'  
count_word_occurrences(file_path)
