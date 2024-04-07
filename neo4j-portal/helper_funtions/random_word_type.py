import re

def word_type_rand(input_data):

    output = ""
    for item in input_data:
        if 'name' in item and item['name'] == 'stdout':
            text = item['text']
            
            # Extracting lemma using regex
            lemma_match = re.search(r"'lemma': '([^']*)'", text)
            if lemma_match:
                lemma = lemma_match.group(1)
            else:
                continue

            # Extracting labels using regex
            labels_match = re.search(r"labels=frozenset\(\{'([^']*)'\}\)", text)
            if labels_match:
                labels = labels_match.group(1)
            else:
                continue

            output += f"{lemma} - {labels}\n"

    return output


