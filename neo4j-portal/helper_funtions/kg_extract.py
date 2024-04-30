import re

def extract_tamil_words(input_string):
    # Define regex pattern for Tamil words
    tamil_pattern = re.compile(r'[அ-ஹ]+')

    # Find all matches in the input string
    tamil_words = tamil_pattern.findall(input_string)

    return tamil_words