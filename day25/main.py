import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for file in filepaths:
    df = pd.read_excel(file, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    filename = Path(file).stem
    invoice_no = filename.split("-")[0]
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice no.{invoice_no}")
    pdf.output(f"PDFs/{filename}.pdf")