import PyPDF2

with open('./Files/dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    # print(reader.numPages)  # Tells us the number of pages in a PDF
    # print(reader.getPage(0))

    page = reader.getPage(0)
    page = page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('./Files/crooked.pdf','wb') as new_file:
        writer.write(new_file)




