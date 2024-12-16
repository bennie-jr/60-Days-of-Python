from fpdf import FPDF
from pathlib import Path
import glob

# Create a list of text file paths
filepaths = glob.glob("files/*.txt")
filepaths.sort()

# Create a single PDF file
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Iterate through each text file
for file in filepaths:
    # Add a page to the PDF document for each text file
    pdf.add_page()

    # Get filename without extension and convert it to title case (e.g. Cat)
    filename = Path(file).stem
    topic = filename.title()

    # Add the name/topic to the PDF
    pdf.set_font(family="Times", size=24, style="B")
    pdf.cell(w=50, h=8, txt=topic, align="L", ln=1 )

# Create the PDF
pdf.output("output.pdf")