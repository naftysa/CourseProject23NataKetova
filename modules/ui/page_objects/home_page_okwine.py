from modules.ui.page_objects.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



class HomePageOkwine(BasePage):
    URL = "https://okwine.ua/ua"
    
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
        wait = WebDriverWait(webdriver.Chrome(), 3)
        
        # Found the link to the product found preview and click it
        found_elem = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Віскі Ардбег Тен / Ardbeg Ten").click()
        wait = WebDriverWait(webdriver.Chrome(), 3)
        
        # Search for the 'Into the cart delivery' button
        found_add_to_cart = self.driver.find_element(By.XPATH, "//*[@id='__next']/div[5]/div/div[2]/div[2]/span/div[2]/div/div[2]/button").click()
        
        # Find and click the cart button in the header
        find_cart_icon = self.driver.find_element(By.XPATH, "//*[@id='__next']/header/div/div[9]/a")
        find_cart_icon.click()
        wait = WebDriverWait(webdriver.Chrome(), 3)
    
        # Find and click the ordered product from cart
        find_order_info_link = self.driver.find_element(By.XPATH, "//*[@id='__next']/div[3]/div/div/div[1]/div[3]/form/div[2]/div[1]/div/ul/div/li/div/div[1]/h4/a")
        find_order_info_link.click()
        wait = WebDriverWait(webdriver.Chrome(), 3)
        
        # Verify that text on the page is that one we expected
    def check_page_text(self, expected_value):
        search_expected_text = self.driver.find_element(By.XPATH, "//*[@id='__next']/div[5]/div/ul/li[3]/a").text
        #print(search_expected_text.encode("UTF-8"))
        return search_expected_text == expected_value
              