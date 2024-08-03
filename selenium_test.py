import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Set up the WebDriver (for Chrome in this case)
driver = webdriver.Chrome()  # Make sure chromedriver is in your PATH or provide the path to it

# Open a webpage
driver.get("https://www.facebook.com")  # Replace with the URL you want to open

# Wait for the page to load
time.sleep(5)  # Adjust the wait time as needed

try:
    # Click on the signup button using CSS selector
    signup = WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a._42ft._4jy0._6lti._4jy6._4jy2.selected._51sy'))
    )
    signup.click()

    # Wait for the first name input field to be present
    first_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'firstname'))
    )
    firstname = input("Please enter your first name: ")
    first_name.send_keys(firstname)

    # Find the last name input field by its name attribute
    last_name = driver.find_element(By.NAME, 'lastname')
    lastname = input("Please enter your last name: ")
    last_name.send_keys(lastname)

    # Find the email/phone input field by its name attribute
    phone_number = driver.find_element(By.NAME, 'reg_email__')
    phonenumber = input("Please enter your Email or your phone: ")
    phone_number.send_keys(phonenumber)

    # Find the password input field by its name attribute
    reg_passwd__ = driver.find_element(By.NAME, 'reg_passwd__')
    regpasswd__ = input("Please enter your password: ")
    reg_passwd__.send_keys(regpasswd__)

    # Find the birthday day input field by its name attribute
    birthday_day = driver.find_element(By.NAME, 'birthday_day')
    birthdayday = input("Please enter your birthday day: ")
    birthday_day.send_keys(birthdayday)

    # Find the birthday month input field by its name attribute
    birthday_month = driver.find_element(By.NAME, 'birthday_month')
    birthdaymonth = input("Please enter your birthday month: ")
    birthday_month.send_keys(birthdaymonth)

    # Find the birthday year input field by its name attribute
    birthday_year = driver.find_element(By.NAME, 'birthday_year')
    birthdayyear = input("Please enter your birthday year: ")
    birthday_year.send_keys(birthdayyear)

    # Select gender based on user input
    gender_input = input("Please enter 1 for Female, 2 for Male, or -1 for Custom: ")
    if gender_input == '1':
        gender = driver.find_element(By.XPATH, "//input[@name='sex' and @value='1']")
    elif gender_input == '2':
        gender = driver.find_element(By.XPATH, "//input[@name='sex' and @value='2']")
    elif gender_input == '-1':
        gender = driver.find_element(By.XPATH, "//input[@name='sex' and @value='-1']")
    else:
        raise ValueError("Invalid input for gender selection")
    gender.click()
    
    signup2 = driver.find_element(By.NAME, 'websubmit')
    signup2.click()


except Exception as e:
    print(f"An error occurred: {e}")

# Close the browser after a delay
time.sleep(100)  # Wait for 100 seconds
driver.quit()  # Close the browser
