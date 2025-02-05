import pandas
from fpdf import FPDF

df = pandas.read_csv("articles.csv", dtype={"id": str})



class Articles:
    def __init__(self, article_id):
        self.article_id = article_id
        self.name = df.loc[df["id"] == self.article_id, "name"].squeeze()
        self.price = df.loc[df["id"] == self.article_id, "price"].squeeze()
        
    

    def purchase(self):
        """purchase an article by reducing its in_stock value by 1"""
        df.loc[df["id"] == self.article_id, "in stock"] = df["in stock"] - 1
        df.to_csv("articles.csv", index=False)

    def available(self):
        """Check if the article is available"""
        availability = df.loc[df["id"] == self.article_id].squeeze()
        # print(availability)
        if not availability.empty:
            return True
        else:
            return False


class PdfReceipt:
    """Print PDF receipt of article purchase"""
    def __init__(self, articles_object):
        self.articles = articles_object


    def generate(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr.1", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.articles.name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.articles.price}", ln=1)

        receipt = pdf.output("receipt.pdf")
        return receipt



print(df)
article_ID = input("Choose an article to buy: ")
article = Articles(article_ID)
if article.available():
    article.purchase()
    pdf_receipt = PdfReceipt(articles_object=article)
    pdf_receipt.generate()
else:
    print("Article isn't available for purchase.")
