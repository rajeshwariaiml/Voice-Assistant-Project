import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wait until the element is clickable
video = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="video-title"]/yt-formatted-string'))
)
video.click()



class music:
    def __init__(self):
        # Create a Service object for ChromeDriver
        service = Service(ChromeDriverManager().install())
        
        # Pass the Service object to the webdriver
        self.driver = webdriver.Chrome(service=service)

    def play(self , query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
        video=self.driver.find_element("xpath", '//*[@id="video-title"]/yt-formatted-string')
        video.click()
        
assist=music()
assist.play('Hanuman')