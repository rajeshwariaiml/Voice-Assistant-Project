import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppress TensorFlow warnings


class music:
    def __init__(self):
        # Create a Service object for ChromeDriver
        service = Service(ChromeDriverManager().install())
        
        # Pass the Service object to the webdriver
        self.driver = webdriver.Chrome(service=service)

    def play(self, query):
        self.query = query
        self.driver.get("https://www.youtube.com/results?search_query=" + query)

        try:
            # Wait for the video element to be clickable
            video = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="video-title"]/yt-formatted-string'))
            )
            video.click()
        except Exception as e:
            print(f"An error occurred: {e}")
        time.sleep(5)  # Give time to watch or close the video if needed
        self.driver.quit()


#assist = music()
#assist.play('Hanuman')
