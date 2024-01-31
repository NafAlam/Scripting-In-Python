import os
from PyPDF2 import PdfReader, PdfWriter

pdf_folder = 'watermark/'
watermark_pdf = 'watermark/wtr.pdf'

watermark_reader = PdfReader(watermark_pdf)
watermark_page = watermark_reader.pages[0]

# Iterate through all files in the folder
for pdf_file in os.listdir(pdf_folder):
    if pdf_file.endswith('.pdf') and pdf_file != os.path.basename(watermark_pdf):
        pdf_path = os.path.join(pdf_folder, pdf_file)
        reader = PdfReader(pdf_path)
        writer = PdfWriter()

        # Add watermark to each page
        for page in reader.pages:
            page.merge_page(watermark_page)
            writer.add_page(page)

        # Write the watermarked PDF to a new file
        watermarked_pdf_path = os.path.join(pdf_folder, f"watermarked_{pdf_file}")
        with open(watermarked_pdf_path, 'wb') as f_out:
            writer.write(f_out)

        print(f"Watermarked {pdf_file} and saved as {watermarked_pdf_path}")
