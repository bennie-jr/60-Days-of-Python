### DAY 24: App 3 - PDF Maker

Today, I built app number 3 which is a PDF Maker.

Recap on what I did yesterday. I added a second page for the Contact Me form which takes the user's email and the 
message and sends it via email. I wrote a script for sending emails which connects to the Contact Me page.
I used the gmail smtp for sending of the emails. Today, I wrote a program that creates a PDF document.


Now to the code I wrote today, I imported the FPDF module to help me generate the pdf document. I had a csv file as 
my data source which I used to create the contents of the pdf. I imported pandas module to help me red the contents
of the csv file. The PDF maker code is supposed to generate a document that contains various topics(as headers) on
python which the user can use to write notes cos the body is blank. I used nested for loops together with the contents
of the csv file which was read with pandas to create pages for each topic because some topics had more pages. I used 
various methods of the FPDF modules to adjust and set contents of the header and footer of the pages. I was able to complete
this app, and it worked like it should.


Also, I completed a [side-project](SP-Lined-PDF-1) where I built on the pdf maker app to create a lined pdf document. The 
pdf document I created earlier had a blank body but this time I added lines to aid with writing making it appear like 
a regular notebook or notepad. I used more nested for loops to help me achieve this. 

Lastly I learnt about the PEP 8 style guide and the best practices to adopt whilst writing python code.


All in all, day 24 was good, I am done building the third application. I will start building app number 4 tomorrow.