from fpdf import FPDF



def main():

    name = input("Name: ")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(False)
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 20, "CS50 Shirtificate", align="C")
    pdf.ln(20)


    w_img = 100
    h_img = 100
    x_img = (pdf.w - w_img) / 2
    y_img = pdf.get_y()


    pdf.image("shirtificate.png", x=x_img, y=y_img, w=w_img, h=h_img)
    pdf.set_font("Helvetica", "", 12)
    pdf.set_text_color(255, 255, 255)
    name_y = y_img + (h_img / 2) - 20
    offset_x = 10
    pdf.set_xy(x_img + offset_x, name_y)
    pdf.cell(w_img - 2 * offset_x, 10, name, align="C")



    pdf.output("shirtificate.pdf")






    









if __name__ == "__main__":
    main()