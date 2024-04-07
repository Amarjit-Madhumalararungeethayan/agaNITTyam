import os
from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
import subprocess
import nbformat

from helper_funtions.random_word_type import word_type_rand

app = Flask(__name__)
toolbar = DebugToolbarExtension(app)

def execute_notebook(notebook_filename, temp):
    
    # Delete previous output notebook file
    output_filename = notebook_filename.replace('.ipynb', '.nbconvert.ipynb')
    if os.path.exists(output_filename):
        os.remove(output_filename)

    command = f"jupyter nbconvert --to notebook --execute {notebook_filename}"
    completed_process = subprocess.run(command, shell=True, capture_output=True, text=True)
    if completed_process.returncode != 0:
        print("Error executing notebook:", completed_process.stderr)
        return None
    
    # Read the notebook content after execution
    with open(temp, 'r') as f:
        notebook_content = nbformat.read(f, as_version=4)

    # Extract output from cells with the specified tag
    tagged_output = []
    for cell in notebook_content.cells:
        if 'tags' in cell.metadata and "capture_output" in cell.metadata.tags:
            if 'outputs' in cell:
                tagged_output.extend(cell.outputs)

    return (tagged_output)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    option = request.form['option']
    print("☆ Chosen Option -> " + option)

    # Depending on the option chosen, sent a request 2 Jupyter
    if option == 'Vaarthai Vagai':
        result = execute_notebook('ran-word.ipynb', 'ran-word.nbconvert.ipynb')
        temp = word_type_rand(result)
        if result is not None:
            # Return the output to the clientr
            return render_template('result.html', result=temp)
        else:
            return "Error executing notebook"
    else:
        return "Invalid option"

    # Check if the execution was successful
    # Assuming execute_notebook() returns some meaningful result
    print("Output from Jupyter Notebook execution:", result)
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)