from selenium import webdriver


class infow():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:\\Users\\rajes\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    
    def get_info(self,query):
        self.query=query
        self.driver.get("http://www.wikipedia.org")
       # search_box = self.driver.find_element("name", "search")
        #search_box.send_keys(query)
        #search_box.submit()
        
        
        
assist=infow()
assist.get_info("hello")