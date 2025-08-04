# Import the PyPDF2 library
import pyPDF2
# Open the input PDF files
with open('C:/Users/suman/OneDrive/Documents/PDF X/DSD book notes - 2025-08-02 14-26-42.pdf', 'rb') as f1, open('C:/Users/suman/OneDrive/Documents/PDF X/Thomas calculus 1 - 2024-08-20 01-00-42.pdf', 'rb') as f2:
    # Create PdfFileReader objects
    reader1 = PdfFileReader(f1)
    reader2 = PdfFileReader(f2)

    # Create a PdfFileWriter object
    writer = PdfFileWriter()

    # Merge the PDF files
    for page in reader1.pages:
        writer.addPage(page)
    for page in reader2.pages:
        writer.addPage(page)

    # Write the merged PDF to a new file
    with open('output.pdf', 'wb') as f:
        writer.write(f)