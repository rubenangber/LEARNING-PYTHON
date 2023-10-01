import PyPDF2

pdf_pass = PyPDF2.PdfFileReader(open('encrypted.pdf'))
with open('passwords.txt', 'r', encoding='utf-8') as f:
    for line in f:
        password = line.strip()
        if pdf_pass.decrypt(password) != 0:
            print(f'Password found: {password}')
            break 