import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class infow:
    def __init__(self):
        # Create a Service object for ChromeDriver
        service = Service(ChromeDriverManager().install())
        
        # Pass the Service object to the webdriver
        self.driver = webdriver.Chrome(service=service)

    def get_info(self, search_query):
        # Open Wikipedia with the search query
        self.search_query = search_query
        self.driver.get("http://www.wikipedia.org")
        search_box = self.driver.find_element("xpath", '//*[@id="searchInput"]')

        search_box.click()
        search_box.send_keys(search_query)
        enter = self.driver.find_element("xpath",'//*[@id="search-form"]/fieldset/button')
        enter.click()
        #search_box.submit()

# Example of using the class


#input("Press Enter to close the browser...")

