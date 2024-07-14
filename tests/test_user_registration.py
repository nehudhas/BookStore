from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open the web application
driver.get("http://127.0.0.1:5000/register")  # Replace with your actual URL

# Test valid registration
def test_valid_registration():
    try:
        # Wait for the username field to be present
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        
        # Print the page source for debugging
        print(driver.page_source)
        
        # Fill out the registration form
        driver.find_element(By.NAME, "username").send_keys("validUser")
        driver.find_element(By.NAME, "email").send_keys("validuser@example.com")
        driver.find_element(By.NAME, "password").send_keys("validPassword123")
        driver.find_element(By.NAME, "confirm_password").send_keys("validPassword123")
        driver.find_element(By.NAME, "submit").click()
        
        # Wait for the registration success message
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Registration successful")
        )
        
        # Check for the success message in the page source
        assert "Registration successful" in driver.page_source, "Expected success message not found in the page source"
    
    except Exception as e:
        print(f"Error: {e}")

# Test invalid registration (e.g., password mismatch)
def test_invalid_registration():
    try:
        # Wait for the username field to be present
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        
        # Fill out the registration form with invalid data
        driver.find_element(By.NAME, "username").send_keys("invalid
