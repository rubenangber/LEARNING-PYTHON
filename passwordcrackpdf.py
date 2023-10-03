import PyPDF2

encryptedpdf = input('Enter the name of the encrypted pdf file: ')
pdf_pass = PyPDF2.PdfFileReader(open(encryptedpdf))
with open('passwords.txt', 'r', encoding = 'utf-8') as f:
    for line in f:
        password = line.strip()
        if pdf_pass.decrypt(password) != 0:
            print(f'Password found: {password}')
            break