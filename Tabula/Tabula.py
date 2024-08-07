import tabula

# Specify the input PDF file
pdf_file = "testing.pdf"

# Specify the output CSV file
csv_file = "finaloutput1.csv"

# Read the PDF file into a list of DataFrames
dfs = tabula.read_pdf(pdf_file, pages='all')

# Convert the DataFrames to a single CSV file
tabula.convert_into(pdf_file, csv_file, output_format="csv", pages='all')


print("Data extracted and saved to", csv_file)