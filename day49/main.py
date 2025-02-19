from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

# Define driver, options, and service
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

# dowload_path = os.getcwd()
# prefs = {'download.default_directory': dowload_path}
# chrome_options.add_experimental_option('prefs', prefs)

service = Service('chromedriver-linux64/chromedriver')
driver = webdriver.Chrome(options=chrome_options, service=service)

# Load the webpage
driver.get('https://thinking-tester-contact-list.herokuapp.com/')

# Locate email, password, and login button
email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'email')))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
# login_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'submit')))
login_button = driver.find_element(By.ID, 'submit')

# Fill in email and password, and click the login button
email_field.send_keys('bensowahjr@gmail.com')
password_field.send_keys('')
# login_button.click()
driver.execute_script("arguments[0].click();", login_button)


# Locate the add contact button and click the button
add_contact = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'add-contact')))
add_contact.click()

# Locate the form fields
first_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'firstName')))
last_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'lastName')))


date_of_birth = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'birthdate'))) 

email = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'email'))) 
phone = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'phone')))

street_address = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'street1')))


city = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'city')))
state_province = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'stateProvince')))


postal_code = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'postalCode')))
country = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'country')))

login_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'submit')))

# Fill in the form fields
first_name.send_keys('Kwame')
last_name.send_keys('Brown')
date_of_birth.send_keys('1800-01-01')
email.send_keys('niijr@outlook.com')
phone.send_keys('111666888')
street_address.send_keys('Mukose street')
city.send_keys('Accra')
state_province.send_keys('Greater Accra')
postal_code.send_keys('002233')
country.send_keys('Ghana')
login_button.click()


input("Press Enter to close the browser")
driver.quit()