import tkinter as tk
from tkinter import messagebox
from main_oop import WebAutomation

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Automation GUI")

        # Login frame
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(padx=10, pady=10)

        tk.Label(self.login_frame, text="Email").grid(row=0, column=0, sticky="w")
        self.entry_login_email = tk.Entry(self.login_frame)
        self.entry_login_email.grid(row=0, column=1, sticky="ew")

        tk.Label(self.login_frame, text="Password").grid(row=1, column=0, sticky="w")
        self.entry_password = tk.Entry(self.login_frame, show="*")
        self.entry_password.grid(row=1, column=1, sticky="ew")

        # Form submission frame
        self.form_frame = tk.Frame(self.root)
        self.form_frame.pack(padx=10, pady=10)

        tk.Label(self.form_frame, text="First Name").grid(row=0, column=0, sticky="w")
        self.entry_first_name = tk.Entry(self.form_frame)
        self.entry_first_name.grid(row=0, column=1, sticky="ew")

        tk.Label(self.form_frame, text="Last Name").grid(row=1, column=0, sticky="w")
        self.entry_last_name = tk.Entry(self.form_frame)
        self.entry_last_name.grid(row=1, column=1, sticky="ew")

        tk.Label(self.form_frame, text="Date of Birth").grid(row=2, column=0, sticky="w")
        self.entry_date_of_birth = tk.Entry(self.form_frame)
        self.entry_date_of_birth.grid(row=2, column=1, sticky="ew")

        tk.Label(self.form_frame, text="Email").grid(row=3, column=0, sticky="w")
        self.entry_email = tk.Entry(self.form_frame)
        self.entry_email.grid(row=3, column=1, sticky="ew")

        tk.Label(self.form_frame, text="Phone Number").grid(row=4, column=0, sticky="w")
        self.entry_phone = tk.Entry(self.form_frame)
        self.entry_phone.grid(row=4, column=1, sticky="ew")

        tk.Label(self.form_frame, text="Street Address").grid(row=5, column=0, sticky="w")
        self.entry_street_address = tk.Entry(self.form_frame)
        self.entry_street_address.grid(row=5, column=1, sticky="ew")

        tk.Label(self.form_frame, text="City").grid(row=6, column=0, sticky="w")
        self.entry_city = tk.Entry(self.form_frame)
        self.entry_city.grid(row=6, column=1, sticky="ew")

        tk.Label(self.form_frame, text="State or Province").grid(row=7, column=0, sticky="w")
        self.entry_state_province = tk.Entry(self.form_frame)
        self.entry_state_province.grid(row=7, column=1, sticky="ew")

        tk.Label(self.form_frame, text="Postal Code").grid(row=8, column=0, sticky="w")
        self.entry_postal_code = tk.Entry(self.form_frame)
        self.entry_postal_code.grid(row=8, column=1, sticky="ew")

        tk.Label(self.form_frame, text="Country").grid(row=9, column=0, sticky="w")
        self.entry_country = tk.Entry(self.form_frame)
        self.entry_country.grid(row=9, column=1, sticky="ew")

        # Buttons
        self.button_frame = tk.Frame()
        self.button_frame.pack(padx=10, pady=10)

        tk.Button(self.button_frame, text="Submit", command=self.submit_data).grid(row=0, column=0, padx=5)
        tk.Button(self.button_frame, text="Close Browser", command=self.close_browser).grid(row=0, column=1, padx=5)




    def submit_data(self):
        login_email = self.entry_login_email.get()
        password = self.entry_password.get()

        first_name = self.entry_first_name.get()
        last_name = self.entry_last_name.get()
        date_of_birth = self.entry_date_of_birth.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get() 
        street_address = self.entry_street_address.get()
        city = self.entry_city.get()
        state_province = self.entry_state_province.get()
        postal_code = self.entry_postal_code.get()
        country = self.entry_country.get()


        self.web_automation = WebAutomation()
        self.web_automation.login(login_email, password)
        self.web_automation.fill_form(first_name, last_name, date_of_birth, email,
                                       phone, street_address, city, state_province, postal_code, country)


    def close_browser(self):
        self.web_automation.close()
        messagebox.showinfo("Browser Close", "Form Submitted Successfully")
        
root = tk.Tk()
app = App(root)
root.mainloop()
