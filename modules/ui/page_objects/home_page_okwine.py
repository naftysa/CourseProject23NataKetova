from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePageOkwine(BasePage):
    URL = "https://okwine.ua/ua"
    
    def __init__(self) -> None:
        super().__init__()
        
    def go_to(self):
        self.driver.get(HomePageOkwine.URL)
        
    def close_is_18_popup(self):
        # Знаходимо поп-ап 'Вам вже виповнилось 18 років?'
        search_tak_btn = self.driver.find_element(By.XPATH, "//*[@id='__next']/footer/div[1]/div/div[1]/a[1]/button")

        # Закриваємо поп-ап кліком миші на кнопку 'ТАК'
        search_tak_btn.click()
        
    def try_add_to_cart(self, productname):
        # Find a search field
        search_elem = self.driver.find_element(By.ID, "integrationSearchBarInput")
        
        # Insert a desired product name into the search field
        search_elem.send_keys(productname)
        
        #  Знаходимо кнопку 'Шукати'
        btn_elem = self.driver.find_element(By.ID, "integrationSearchGoButton")
        
        # Емулюємо клік ліваю кнопкою миші
        btn_elem.click()
        
        # Знаходимо кнопку 'Додати до кошика' в знайденому продукті
        found_elem = self.driver.find_element(By.ID, "integrationAddProductButton")
        
        # Емулюємо клік лівою кнопкою миші
        found_elem.click()
        
        # У вікні знаходимо кнопку 'В корзину'
        found_add_to_cart = self.driver.find_element(By.ID, "addToCartDeliveryButton")
        
        # Емулюємо клік лівою кнопкою миші
        found_add_to_cart.click()
        
        # Знаходимо кнопку 'Оформити замовлення'
        found_go_to_cart = self.driver.find_element(By.ID, "modalSubmit")

        # Емулюємо клік лівою кнопкою миші
        found_go_to_cart.click()
        
    def check_order_text(self, expected_text):
        return self.driver.find_element(By.NAME, "integrationCustomerInformation") == expected_text
          