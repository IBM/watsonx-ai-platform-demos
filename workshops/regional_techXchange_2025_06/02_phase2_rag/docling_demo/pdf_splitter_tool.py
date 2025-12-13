import sys
import PyPDF2

def extract_pages(input_pdf, start_page, end_page, output_pdf):
    try:
        with open(input_pdf, 'rb') as infile:
            reader = PyPDF2.PdfReader(infile)
            writer = PyPDF2.PdfWriter()
            num_pages = len(reader.pages)

            # Adjust for 1-based page numbers
            start = max(0, start_page - 1)
            end = min(end_page, num_pages)

            if start >= end or start < 0 or end > num_pages:
                print(f"Invalid page range: {start_page}-{end_page} for PDF with {num_pages} pages.")
                return

            for i in range(start, end):
                writer.add_page(reader.pages[i])

            with open(output_pdf, 'wb') as outfile:
                writer.write(outfile)
            print(f"Pages {start_page}-{end_page} extracted to {output_pdf}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python pdf_splitter_tool.py <input.pdf> <start_page> <end_page> <output.pdf>")
        sys.exit(1)
    input_pdf = sys.argv[1]
    try:
        start_page = int(sys.argv[2])
        end_page = int(sys.argv[3])
    except ValueError:
        print("Start and end pages must be integers.")
        sys.exit(1)
    output_pdf = sys.argv[4]
    extract_pages(input_pdf, start_page, end_page, output_pdf)


