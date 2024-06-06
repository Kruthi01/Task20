from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Open the URL
driver.get("https://www.cowin.gov.in/")
# Function to switch to a new window
def switch_to_new_window():
    # Get handles of all windows
    handles = driver.window_handles
    # Switch to the new window
    driver.switch_to.window(handles[-1])

# Click on FAQ link
faq_link = driver.find_element(By.XPATH,'//*[@id="navbar"]/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[4]/a')
faq_link.click()

# Wait for the new window to open
time.sleep(3)

# Fetch and display the ID of the new window
switch_to_new_window()
print("FAQ Window ID:", driver.current_window_handle)

# Close the new window
driver.close()

# Switch back to the original window
driver.switch_to.window(driver.window_handles[0])

# Click on Partners link
partners_link = driver.find_element(By.XPATH,'//*[@id="navbar"]/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a')
partners_link.click()

# Wait for the new window to open
time.sleep(3)

# Fetch and display the ID of the new window
switch_to_new_window()
print("Partners Window ID:", driver.current_window_handle)

# Close the new window
driver.close()

# Switch back to the original window
driver.switch_to.window(driver.window_handles[0])

# Close the browser
driver.quit()
