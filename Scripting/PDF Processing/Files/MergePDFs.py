import sys

import PyPDF2

# run this program from CLI: pass arguments as path and name of pdf file to merge all of them
# Order of arguments matters here
inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')


pdf_combiner(inputs)
