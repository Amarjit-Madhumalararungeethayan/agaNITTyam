import os
from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
import subprocess
import nbformat
import random

from helper_funtions.random_word_type import word_type_rand
from helper_funtions.synonym import synonym_gen
from helper_funtions.option_generator import choose_random_words

app = Flask(__name__, static_url_path='/static', static_folder='static')
toolbar = DebugToolbarExtension(app)
curr_note = ""

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

@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    option = request.form['option']
    print("☆ Chosen Option -> " + option)

    # option Type of Word
    if option == 'Vaarthai Vagai':
        types = ["இடப்பெயர்", "காலப்பெயர்", "சினைப்பெயர்", "தொழிற்பெயர்", "பொருட்பெயர்", "பண்புப்பெயர்"]
        random.shuffle(types)
        result = execute_notebook('ran-word.ipynb', 'ran-word.nbconvert.ipynb')
        temp = word_type_rand(result)
        if result is not None:
            # Return the output to the clientr
            res = temp.split(" - ")
            res.append(option)
            res.append(types)
            return render_template('ran-word-result.html', result=res)
        
        else:
            return "Error executing notebook"
    
    elif option == "Synonym":
        result = execute_notebook('synonym.ipynb', 'synonym.nbconvert.ipynb')
        temp = synonym_gen(result)
        if result is not None:
            # Return the output to the clientr
            res = temp.split('\\t')
            options = choose_random_words()
            if temp in options:
               options.remove(temp)
            print(options)
            for word in options:
                res.append(word)

            ans = res[1]
            copy = res[1:]
            random.shuffle(copy)
            res[1:] = copy # overwrite the original
            res.append(ans)

            return render_template('synonym-result.html', result=res)

    elif option == "Plural":
        result = execute_notebook('plural.ipynb', 'plural.nbconvert.ipynb')
        temp = synonym_gen(result)
        if result is not None:
            # Return the output to the clientr
            res = temp.split('\\t')
            options = [res[0]+"க்கள்", res[0]+"ங்கள்", res[0]+"டுகள்", res[0]+"ய்கள்", res[0]+"வர்கள்", res[0]+"ர்கள்", res[0]+"கல்", res[0]+"கழ்", res[0]+"எல்"]
            random.shuffle(options)
            options = options[0:3]
            if temp in options:
               options.remove(temp)
               
            for word in options:
                res.append(word)

            ans = res[1]
            copy = res[1:]
            random.shuffle(copy)
            res[1:] = copy # overwrite the original
            res.append(ans)

            return render_template('plural-result.html', result=res)

    elif option == "Opposite":
            result = execute_notebook('opposite.ipynb', 'opposite.nbconvert.ipynb')
            temp = synonym_gen(result)
            if result is not None:
                # Return the output to the clientr
                res = temp.split('\\t')
                options = choose_random_words()
                if temp in options:
                    options.remove(temp)
                print(options)
                for word in options:
                    res.append(word)

                ans = res[1]
                copy = res[1:]
                random.shuffle(copy)
                res[1:] = copy # overwrite the original
                res.append(ans)

                return render_template('opposite-result.html', result=res)
            
    elif option == "Pirithu":
            result = execute_notebook('pirithu.ipynb', 'pirithu.nbconvert.ipynb')
            temp = synonym_gen(result)
            print(temp)
            res = temp.split('\\t')
            return render_template('pirithu-result.html', result=res)
    
    elif option == "Tenses":
            #result = execute_notebook('tenses.ipynb', 'tenses.nbconvert.ipynb')
            #temp = synonym_gen(result)
            #print(temp)
            #res = temp.split('\\t')
            res = ["வந்தேன்", "வருகிறேன்", "வருவேன்"]
            print(res)

            options = res[0:3]
            random.shuffle(options)
            
            for word in options:
                res.append(word)

            return render_template('tenses-result.html', result=res)
    
    elif option == "KG":
            #result = execute_notebook('tenses.ipynb', 'tenses.nbconvert.ipynb')
            #temp = synonym_gen(result)
            #print(temp)
            #res = temp.split('\\t')
            res = ["வந்தேன்", "வருகிறேன்", "வருவேன்"]
            print(res)

            options = res[0:3]
            random.shuffle(options)
            
            for word in options:
                res.append(word)

            return render_template('kg-result.html')

    else:
        return "Invalid option"

if __name__ == '__main__':
    app.run(debug=True)