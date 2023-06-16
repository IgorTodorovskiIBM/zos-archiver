import os
import PyPDF2

def convert_pdf_to_text(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        text = ''
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
        return text

def convert_directory_to_text(directory_path):
    text_output_directory = 'text_output'
    os.makedirs(text_output_directory, exist_ok=True)
    
    for filename in os.listdir(directory_path):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(directory_path, filename)
            text = convert_pdf_to_text(pdf_path)
            
            text_filename = os.path.splitext(filename)[0] + '.txt'
            text_filepath = os.path.join(text_output_directory, text_filename)
            
            with open(text_filepath, 'w', encoding='utf-8') as text_file:
                text_file.write(text)
            
            print(f'Converted {filename} to {text_filename}')

# Provide the directory path containing the PDF files
directory_path = '/path/to/pdf/files'

# Convert the PDF files to text
convert_directory_to_text(directory_path)
