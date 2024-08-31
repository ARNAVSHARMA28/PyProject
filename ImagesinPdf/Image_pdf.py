from io import BytesIO
import cv2
import pandas as pd

from img2table.document import PDF

pdf_path = "C:\\Users\\Arnav_Sharma\\PyProj\\pdfimg.pdf"

# Definition of PDF from path
# The optional pages argument enables the extraction of table on specific pages of the PDF
pdf_from_path = PDF(src=pdf_path, pages=[0, 1])

# Definition of PDF from bytes
with open(pdf_path, 'rb') as f:
    pdf_bytes = f.read()
pdf_from_bytes = PDF(src=pdf_bytes)

# Definition of PDF from file-like object
pdf_from_file_like = PDF(src=BytesIO(pdf_bytes))

# Tesseract OCR
from img2table.ocr import TesseractOCR

tesseract_ocr = TesseractOCR(n_threads=1, lang="eng")

pdf = PDF(src="C:\\Users\\Arnav_Sharma\\PyProj\\pdfimg.pdf")

# Extract tables
extracted_tables = pdf.extract_tables(ocr=tesseract_ocr,
                                      implicit_rows=False,
                                      borderless_tables=False,
                                      min_confidence=50)


# Save extracted tables to a single CSV file
df_combined = pd.concat([pd.DataFrame(table.df) for tables in extracted_tables.values() for table in tables])
df_combined.to_csv("all_tables1.csv", index=False)        


# Extract tables
extracted_tables = pdf.extract_tables()
