import csv
import ast

def is_python_code(text):
    try:
        ast.parse(text)
        return True
    except SyntaxError:
        return False

def detect_python_code_in_csv(file_path):
    python_code_list = []

    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            for cell in row:
                if is_python_code(cell):
                    python_code_list.append(cell)

    return python_code_list


csv_path = input("Dime el archivo .csv:\n")
python_code_detected = detect_python_code_in_csv(csv_path)

for code in python_code_detected:
    print("Código Python detectado:")
    print(code)
    print("-" * 20)
