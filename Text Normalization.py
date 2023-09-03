import openpyxl
# if your dataset is CSV you can change the prossess from XLSX to CSV
def nettoyer_texte(texte):
    texte = texte.lower()
	# you can add what you need for cleaning you dataset
    return texte
def load_data(filepath):
    try:
        workbook = openpyxl.load_workbook(filepath)
        sheet = workbook.active
        # Extract questions and answers
        data = [nettoyer_texte(str(sheet['A' + str(i)].value)) for i in range(1, sheet.max_row + 1)]
        return data
    except Exception as e:
        print(f"Error reading XLSX file: {e}")
        return []
def count_duplicates(data, output_file_path):
    duplicate_count = 0  # Counter for duplicates
    with open(output_file_path, 'w') as file:
        for i, current_data in enumerate(data):
            for j, other_data in enumerate(data[i+1:], start=i+2):
                if current_data == other_data:
                    duplicate_count += 1
                    file.write(f"'{current_data}' found again at index {j}\n")
                    break
        # Write total duplicates to the file
        file.write(f"\nTotal number of duplicate data: {duplicate_count}")
    return output_file_path
# Example usage:
file_path = '...../YOUR_DATASET.xlsx'
output_path = '....YOUR_PATH/duplicates.txt'
dataset = load_data(file_path)
count_duplicates(dataset, output_path)
