import random
import os

def choose_random_words():

    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, '..', 'static', 'AllTamilWords.txt')

    with open(file_path, 'r', encoding="utf-8") as file:
        words = file.read().split()

    # Remove duplicates and convert to lowercase
    unique_words = list(set([word.lower() for word in words]))

    # Remove the word to avoid
    #if avoid_word.lower() in unique_words:
    #   unique_words.remove(avoid_word.lower())

    # Choose 3 random words
    random_words = random.sample(unique_words, min(3, len(unique_words)))

    return random_words