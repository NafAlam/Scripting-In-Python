import PyPDF2
import sys

paths = sys.argv[1:]
output = "pdf/combined.pdf"
merger = PyPDF2.PdfMerger()

for pdf in paths:
    merger.append(pdf)
merger.write(output)

