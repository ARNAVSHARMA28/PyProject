import pdfplumber
import pandas as pd

def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
        return text

def convert_text_to_table(text):
    lines = text.split('\n')
    data = []
    for line in lines:
        if line.strip():  # ignore empty lines
            data.append(line.split())

    if len(data) > 1 and len(data[0]) == len(data[1]):
        columns = data[0]
        data = data[1:]
    else:
        columns = [f'Column {i+1}' for i in range(len(data[0]))]
    df = pd.DataFrame(data, columns=columns)
    return df

def main():
    file_path = "example1.pdf"
    text = extract_text_from_pdf(file_path)
    df = convert_text_to_table(text)
    print(df)
    df.to_csv('output.csv', index=False)

if __name__ == "__main__":
    main()