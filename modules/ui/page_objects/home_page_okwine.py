from modules.ui.page_objects.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



class HomePageOkwine(BasePage):
    URL = "https://okwine.ua/ua"
    
    #wait = WebDriverWait(webdriver.Chrome(), 10)
    
    def __init__(self) -> None:
        super().__init__()
        
    def go_to(self):
        self.driver.get(HomePageOkwine.URL)
        
    def close_is_18_popup(self):
        # Found pop-up 'Are you 18? Y/N' and click it
        search_tak_btn = self.driver.find_element(By.XPATH, "//*[@id='__next']/footer/div[1]/div/div[1]/a[1]/button").click()
        
    def try_add_to_cart(self, productname):
        # Find a search field
        search_elem = self.driver.find_element(By.XPATH, "//*[@id='__next']/header/div/div[5]/form/input")
        
        # Insert a desired product name into the search field
        search_elem.send_keys(productname)
        
        # Finding the search button and click it
        btn_elem = self.driver.find_element(By.XPATH, "//*[@id='__next']/header/div/div[5]/form/button[1]").click()
        time.sleep(7)
        
        # Found the link to the product found preview and click it
        found_elem = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Віскі Ардбег Тен / Ardbeg Ten").click()
        time.sleep(7)
        
        # Search for the 'Into the cart delivery' button
        found_add_to_cart = self.driver.find_element(By.XPATH, "//*[@id='__next']/div[5]/div/div[2]/div[2]/span/div[2]/div/div[2]/button").click()

        # Verify that text on the button is 'Деталі доставки'
    def check_delivery_button_text(self, expected_value):
        search_cart_icon_counter = self.driver.find_element(By.XPATH, "//*[@id='__next']/div[5]/div/div[2]/div[2]/span/div[2]/div/div[2]/button/text()")
        print(search_cart_icon_counter.text)
        return search_cart_icon_counter.text == expected_value

        
          