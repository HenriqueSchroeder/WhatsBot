import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Chrome:
    """ 
        Controlador do Chrome
    """
    def __init__(self, cookies=True, hidden=False):
        self.cookies = cookies
        self.hidden = hidden
        
        dir_path = os.getcwd()
        profile = os.path.join(dir_path, "profile", "wpp")

        self.chromedriver = Service(ChromeDriverManager().install())

        self.options = webdriver.ChromeOptions()
        
        if self.cookies:
            self.options.add_argument(rf"user-data-dir={profile}")
        
        if self.hidden:
            self.options.add_argument('--headless')
            
        self.options.add_argument('lang=pt-br')
        self.options.add_argument('ignore-certificate-errors')
        self.options.add_argument('--log-level=3')
        self.options.add_experimental_option("excludeSwitches", ["enable-logging"])

        self.driver = webdriver.Chrome(executable_path=self.chromedriver.path, chrome_options=self.options)
        
    