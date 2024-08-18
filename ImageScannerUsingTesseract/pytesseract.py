import pdf2image
import pytesseract
import csv

pdf_file = 'tablefinal.pdf'

images = pdf2image.convert_from_path(pdf_file)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

tables = []
for image in images:
    text = pytesseract.image_to_string(image)
    tables.append(text)

with open('outputtablefinal.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for table in tables:
        rows = table.split('\n')
        for row in rows:
            writer.writerow([row])