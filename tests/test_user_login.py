from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open the web application
driver.get("http://127.0.0.1:5000/login")

# Test valid login
def test_valid_login():
    try:
        # Wait for the username field to be present
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        
        # Print the page source for debugging
        print(driver.page_source)
        
        # Fill out the login form
        driver.find_element(By.NAME, "username").send_keys("validUser")
        driver.find_element(By.NAME, "password").send_keys("validPassword123")
        driver.find_element(By.NAME, "submit").click()
        
        # Wait for the login success message
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Welcome validUser")
        )
        
        # Check for the success message in the page source
        assert "Welcome validUser" in driver.page_source, "Expected success message not found in the page source"
    
    except Exception as e:
        print(f"Error: {e}")

# Test invalid login
def test_invalid_login():
    try:
        # Wait for the username field to be present
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        
        # Fill out the login form with invalid data
        driver.find_element(By.NAME, "username").send_keys("invalidUser")
        driver.find_element(By.NAME, "password").send_keys("invalidPassword")
        driver.find_element(By.NAME, "submit").click()
        
        # Wait for the login error message
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Invalid credentials")
        )
        
        # Check for the error message in the page source
        assert "Invalid credentials" in driver.page_source, "Expected error message not found in the page source"
    
    except Exception as e:
        print(f"Error: {e}")

# Run tests
test_valid_login()
test_invalid_login()

# Close the browser
driver.quit()
