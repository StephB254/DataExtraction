import os
import sys
import comtypes.client

# Function to convert Word document to PDF
def convert_to_pdf(word_file, pdf_file):
    try:
        # Initialize Word application
        word = comtypes.client.CreateObject('Word.Application')

        # Open the Word document
        doc = word.Documents.Open(os.path.abspath(word_file))

        # Save the document as PDF
        doc.SaveAs(os.path.abspath(pdf_file), FileFormat=17)  # FileFormat=17 corresponds to PDF

        # Close the Word document
        doc.Close()

        # Quit Word application
        word.Quit()
        print(f"Converted '{word_file}' to '{pdf_file}' successfully.")
    except Exception as e:
        print(f"Error converting Word to PDF: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_word_to_pdf.py input_word_file output_pdf_file")
    else:
        input_word_file = sys.argv[1]
        output_pdf_file = sys.argv[2]
        convert_to_pdf(input_word_file, output_pdf_file)

# How to use 

#python3 convert_word_to_pdf.py input.docx output.pdf

