### DAY 26: App 4 - Build an Excel to PDF Invoice Generator(Part 2)

Today, I finished building app number 4 which is an Excel to PDF Invoice Generator.

Recap on what I did yesterday. I started building the invoice generator. I imported glob 
and Path from pathlib to help me get the filepaths which I manipulated to get the name for each of the invoice 
PDFs and the invoice numbers. I had to use a for loop to iterate through each file to generate a separate PDF 
for each invoice. In the for loop, I read the Excel file with pandas, created a PDF page for each invoice and 
manipulated the filepaths to get invoice numbers for each invoice and the PDF names for each invoice. Today, I picked 
up from where I left off yesterday.

Now to the code I wrote today, I added the date to the PDF page. I did this by adding the date variable to the invoice
number variable since splitting by hypen would give me two objects in a list and having two variable names would correspond 
to their respective objects. The Excel files were named based on the invoice number and date so it made it easier to get
both. I also added the table from the Excel to the PDF. I was able to do this by using a nested for loop in the main 
for loop and the cell method from FPDF. I added a border to the cells to give it that Excel Spreadsheet look and by 
adjusting the cell sizes for each row, the for loop was able to populate the PDF with the contents of each table. Next, I
added the table header and the total price. I followed the same format I used with importing the table contents but this
time I took it out of the nested for loop since it had to be populated once. I used the .columns method from pandas to
the header from the dataframe and used the sum() method to get the total price. I was able to complete the app and the 
PDF outputs came out like I expected.


Also, I finished building [side-project](SP-Text-Files-to-PDF) which generates a pdf document from text files. After getting the output
title of each pdf page from the names of the texted files yesterday, I added the contents of each txt file to each
PDF page today. I was able to achieve this by using the with open() method in the for loop to read the contents of each
file and the multi_cell() method from FPDF helped populate each page with its respective contents. I used pdf.multi_cell()
method because it was made for bigger pieces of texts that expand across multiple lines. The output PDF came out like
I expected and I was able to finish this side project

Lastly I learnt about using the PyCharm Debugger tool.


All in all, day 26 was good, I am learning more and more each day. I start building app number 5 tomorrow.