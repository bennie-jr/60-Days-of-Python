### DAY 25: App 4 - Build an Excel to PDF Invoice Generator(Part 1)

Today, I started building app number 4 which is an Excel to PDF Invoice Generator.

Recap on what I did yesterday. I wrote a program that creates a PDF document. Today I started building the 
invoice generator.


Now to the code I wrote today, I imported the FPDF module to help me generate the pdf document. I had an Excel file as 
my data source which I will use to generate the contents of the invoice. I imported pandas module to help me read the contents
of the Excel file. I also imported glob and Path from pathlib to help me get the filepaths which I manipulated to
get the name for each of the invoice PDFs and the invoice numbers. Since I was working with multiple files I had to use 
a for loop to iterate through each file to generate a separate PDF for each invoice. In the for loop, I read the Excel file
with pandas, created a PDF page for each invoice and manipulated the filepaths to get invoice numbers for each invoice and the
PDF names for each invoice. That is all I did today, I will continue tomorrow.


Also, I started a building [side-project](SP-Text-Files-to-PDF) which generates a pdf document from text files. The approach
is similar to the PDF Invoice Generator but the only difference is all the text files goes into one pdf document
(i.e. one text file per PDF page). I used a for loop here as well to create the PDF pages and manipulated the filepaths to 
get the title for each page of the PDF. This is what I have done so far, I was able to output the PDF document and the output
document showed exactly what i wrote the code to output.

Lastly I learnt about the Zen of Python.


All in all, day 25 was good, I am learning more and more each day. I will continue building app number 4 tomorrow.