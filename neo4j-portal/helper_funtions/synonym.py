import re

def synonym_gen(input_data):

    output = ""
    for item in input_data:
        if 'name' in item and item['name'] == 'stdout':
            text = item['text']

            # Extracting labels using regex
            labels_match = re.search(r"'line_text': '([^']*)'", text)
            if labels_match:
                labels = labels_match.group(1)
            else:
                continue

            output += f"{labels}\n"

    return output


