import PyPDF2

source = PyPDF2.PdfFileReader(open('./super.pdf', 'rb'))

water_mark = PyPDF2.PdfFileReader(open('./Files/wtr.pdf', 'rb'))

output = PyPDF2.PdfFileWriter()

for i in range(source.getNumPages()):
    page = source.getPage(i)
    page.mergePage(water_mark.getPage(0))
    output.addPage(page)

    with open('super_watermarked.pdf', 'wb') as file:
        output.write(file)

