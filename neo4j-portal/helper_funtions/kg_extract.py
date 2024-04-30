def extract_main_tamil_word(output):
    # Extracting the dictionary from the list
    dictionary = output[0]
    # Extracting the value of 'text' key from the dictionary
    text = dictionary.get('text', '')
    # Extracting the main Tamil word from the 'text' value
    main_word = text.split("'")[1] if "'" in text else None
    return main_word