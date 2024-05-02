import argparse
import papermill as pm
import nbformat
import re
from nbformat.reader import NotJSONError

def word_type_rand(input_data):
    output = ""
    for item in input_data:
        if 'name' in item and item['name'] == 'stdout':
            text = item['text']
            lemma_match = re.search(r"'lemma': '([^']*)'", text)
            if lemma_match:
                lemma = lemma_match.group(1)
            else:
                continue
            labels_match = re.search(r"labels=frozenset\(\{'([^']*)'\}\)", text)
            if labels_match:
                labels = labels_match.group(1)
            else:
                continue
            output += f"{lemma} - {labels}\n"
    return output

def execute_notebook_multiple_times(notebook_path, num_runs):

    all_words = []

    for i in range(num_runs):
        try:
            pm.execute_notebook(notebook_path, 'output.ipynb')

            with open('output.ipynb', 'r', encoding='utf-8') as f:
                output_nb = nbformat.read(f, as_version=4)
            fetched_words = []
            for cell in output_nb.cells:
                if 'tags' in cell.metadata and 'capture_output' in cell.metadata.tags:
                    if cell.cell_type == 'code' and 'outputs' in cell:
                        for output in cell['outputs']:
                            if 'text' in output:
                                fetched_words.append(output['text'])

            all_words.extend(fetched_words)
            
            print(f"Iteration {i+1}: {fetched_words}")

        except NotJSONError as e:
            print(f"Error executing notebook: {e}")
            continue

    num_unique_words = len(set(all_words))
    randomness_score = num_unique_words / num_runs

    return randomness_score

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calc Randomness Score of agaNITTyam')
    parser.add_argument('notebook_path', type=str, help='Path to the Jupyter notebook file')
    parser.add_argument('num_runs', type=int, help='Number of times to run the notebook')
    args = parser.parse_args()

    notebook_path = args.notebook_path
    num_runs = args.num_runs

    randomness_score = execute_notebook_multiple_times(notebook_path, num_runs)
    print(f'Randomness Score: {randomness_score:.2f}')
