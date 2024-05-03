import re
import openpyxl

def calculate_data_accuracy(text_file_path, excel_file_path):

    text_data = []
    excel_data = {}

    # Read text data
    try:
        with open(text_file_path, 'r', encoding='utf-8') as text_file:
            text_data = text_file.readlines()
    except FileNotFoundError:
        print(f"Error: Text file not found at {text_file_path}")
        return None

    # Read excel data
    try:
        workbook = openpyxl.load_workbook(excel_file_path)
        worksheet = workbook.active
        for row in worksheet.iter_rows(min_row=2):  # Skip header row (assuming row 1)
            excel_data[row[0].value] = row[1].value
    except FileNotFoundError:
        print(f"Error: Excel file not found at {excel_file_path}")
        return None

    total_iterations = len(text_data)
    correct_hits = 0

    for line in text_data:
        pair_match = re.search(r'\[(.*?)\]', line)  # Extract Tamil pair within square brackets
        if pair_match:
            pair = pair_match.group(1)
            first_word, second_word = pair.split(' - ')
            first_word = first_word[1:]
            if first_word in excel_data:
                correct_hits += 1
                print(first_word)

    accuracy = correct_hits / total_iterations if total_iterations != 0 else 0

    print(f"Total iterations: {total_iterations}")
    print(f"Correct hits: {correct_hits}")
    print(f"Accuracy: {accuracy:.2%}")

# Example usage
text_file_path = input("Enter text file path: ")
excel_file_path = input("Enter excel file path: ")

calculate_data_accuracy(text_file_path, excel_file_path)
