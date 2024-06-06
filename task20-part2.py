import os
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Open the URL
driver.get("https://labour.gov.in/")
# Wait for the page to load
time.sleep(3)

# Function to create a folder if it doesn't exist
def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

# Function to download file
def download_file(url, folder_name):
    r = requests.get(url)
    file_name = url.split("/")[-1]
    file_path = os.path.join(folder_name, file_name)
    with open(file_path, 'wb') as f:
        f.write(r.content)

# Create a folder to store downloaded files
folder_name = "labour_website_downloads"
create_folder(folder_name)

# Go to the "Documents" menu and download the monthly progress report
documents_menu = driver.find_element(By.XPATH,'//*[@id="nav"]/li[7]/a')
documents_menu.click()
time.sleep(2)

monthly_progress_report_link = driver.find_element(By.XPATH,'//*[@id="nav"]/li[7]/a')
monthly_progress_report_link.click()
time.sleep(2)

# Get the download link
download_link = driver.find_element(By.XPATH,'//*[@id="fontSize"]/div/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/a')
report_url = download_link.get_attribute("href")

# Download the monthly progress report
download_file(report_url, folder_name)

# Go back to the home page
driver.get("https://labour.gov.in/")

# Go to the "Media" menu and navigate to "Photo Gallery"
media_menu = driver.find_element(By.XPATH,'//*[@id="nav"]/li[10]/a')
photo_gallery_sub_menu = driver.find_element(By.XPATH,'//*[@id="block-block-88"]/ul/li[2]/strong/a')

# Move to "Media" menu
ActionChains(driver).move_to_element(media_menu).perform()
time.sleep(2)

# Click on "Photo Gallery"
photo_gallery_sub_menu.click()
time.sleep(2)

# Find and download 10 photos
photo_links = driver.find_elements(By.XPATH,'//*[@id="fontSize"]/div/div/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/table/tbody/tr[1]/td[1]/div[1]/div/img')
for i, photo_link in enumerate(photo_links[:10], start=1):
    photo_url = photo_link.get_attribute("src")
    download_file(photo_url, folder_name)

# Close the browser
driver.quit()
