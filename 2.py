from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to the ChromeDriver executable
driver = webdriver.Chrome()
# Open a website and Navigate to the FitPeo Homepage
driver.get('https://www.fitpeo.com/')
sleep(2)
print("Opened FitPeo Homepage")
# Maximize the browser window
driver.maximize_window()
sleep(3)
# Navigate to the Revenue Calculator Page
try:
    calculator = driver.find_element(By.LINK_TEXT, "Revenue Calculator")
    calculator.click()
    # Check if the element is displayed
    if calculator.is_displayed():
        print("Revenue Calculator is clickable.")
    else:
        print("Revenue Calculator is not visible.")
except Exception as e:
    print("An error occurred:", e)
sleep(2)
# Scroll Down to the Slider section
driver.execute_script("window.scrollBy(0, 250);")

try:
    # Locate the element
    a = driver.find_element(By.ID, ":r0:")

    # Check if the element is displayed
    if a.is_displayed():
        print("Element is visible and clickable.")
        a.click()
        # Clear any existing text in the input field
        a.send_keys(Keys.BACKSPACE * 4)

        # Send the new value to the input field
        a.send_keys("560")
    else:
        print("Element is not visible.")
except Exception as e:
    print("An error occurred:", e)

sleep(5)
driver.execute_script("window.scrollBy(0, 500);")
sleep(5)

# Select CPT Codes like:"CPT-99091", "CPT-99453", "CPT-99454", "CPT-99474"
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for index in [0, 1, 2, 7]:
    if not checkboxes[index].is_selected():
        checkboxes[index].click()
driver.execute_script("window.scrollBy(0, 250);")
sleep(3)
driver.execute_script("window.scrollBy(0, -1500);")
sleep(3)
# Total Reimbursement
try:
    TotalGross = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".MuiTypography-root.MuiTypography-body2.inter.css-1msk7rm"))
    )

    # Check if the element is displayed
    if TotalGross.is_displayed():
        print("Total Revenue displayed")
        sleep(5)
    else:
        print("Total Revenue exists but is not visible.")
except NoSuchElementException:
    print(" Total Gross Revenue Per Year not found.")
finally:
    driver.quit()
