from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


class WebAutomation:
    def __init__(self):
        # Define driver, options, and service
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")

        
        service = Service('chromedriver-linux64/chromedriver')
        self.driver = webdriver.Chrome(options=chrome_options, service=service)

    def login(self, email, password):
        # Load the webpage
        self.driver.get('https://thinking-tester-contact-list.herokuapp.com/')

        # Locate email, password, and login button
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'email')))
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
        # login_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'submit')))
        login_button = self.driver.find_element(By.ID, 'submit')

        # Fill in email and password, and click the login button
        email_field.send_keys(email)
        password_field.send_keys(password)
        # login_button.click()
        self.driver.execute_script("arguments[0].click();", login_button)

    def fill_form(self, first_name, last_name, date_of_birth, email, phone, 
                  street_address, city, state_province, postal_code, country):
        # Locate the add contact button and click the button
        add_contact = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'add-contact')))
        add_contact.click()

        # Locate the form fields
        first_name_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'firstName')))
        last_name_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'lastName')))


        date_of_birth_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'birthdate'))) 

        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'email'))) 
        phone_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'phone')))

        street_address_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'street1')))


        city_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'city')))
        state_province_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'stateProvince')))


        postal_code_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'postalCode')))
        country_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'country')))

        login_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'submit')))

        # Fill in the form fields
        first_name_field.send_keys(first_name)
        last_name_field.send_keys(last_name)
        date_of_birth_field.send_keys(date_of_birth)
        email_field.send_keys(email)
        phone_field.send_keys(phone)
        street_address_field.send_keys(street_address)
        city_field.send_keys(city)
        state_province_field.send_keys(state_province)
        postal_code_field.send_keys(postal_code)
        country_field.send_keys(country)
        login_button.click()


    def close(self):
        self.driver.quit()


if __name__ == "__main__":
    web_automation = WebAutomation()
    web_automation.login('bensowahjr@gmail.com', '')
    web_automation.fill_form("Kwame", "Brown", "1800-01-01", "niijr@outlook.com",
                            "111666888", "Mukose street", "Accra" , "Greater Accra", "002233", "Ghana")
    web_automation.close()






