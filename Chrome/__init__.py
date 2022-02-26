import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Chrome:
    """ 
        Controlador do Chrome
    """

    def __init__(self, cookies=True, hidden=False):
        self.cookies = cookies  # se mantem os cookies da sessão
        self.hidden = hidden  # se faz com que o selenium não mostra a tela do Chrome

        dir_path = os.getcwd()  # pega todo o diretório
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
        self.options.add_experimental_option(
            "excludeSwitches", ["enable-logging"])

        self.driver = webdriver.Chrome(
            executable_path=self.chromedriver.path, chrome_options=self.options)

    def decor_onload(self, *args_, **kwargs_):
        def sub(_self, *args, **kwargs):
            self(_self, *args, **kwargs)
            _self.onload()
        return sub

    def onload(self):
        self.driver.execute_script("window.onload = console.log()")

    def select_element(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def send_key(self, xpath, valor):
        element = self.select_element(xpath)
        element.send_keys(valor)

    def send_key_clear(self, xpath, valor):
        element = self.select_element(xpath)
        element.clear()
        element.send_keys(valor)

    @decor_onload
    def get(self, url: str):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()

    @property
    def title(self):
        return self.driver.title
