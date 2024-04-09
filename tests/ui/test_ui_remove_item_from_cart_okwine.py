from modules.ui.page_objects.home_page_okwine import HomePageOkwine
import pytest


@pytest.mark.uii
def test_check_product_added_to_cart():
    # Створення об'єкту сторінки
    add_to_cart_page = HomePageOkwine()
    
    # Відкриваємо сторінку
    add_to_cart_page.go_to()
    
    # закриття 'Вам вже виповнилось 18 років?' поп-ап
    add_to_cart_page.close_is_18_popup()
    
    # Додаємо продукт в корзину та преходимо в корзину
    add_to_cart_page.try_add_to_cart("Віскі Ардбег Тен")
    
    # Видаляємо продукт з корзини та перевіряємо, шо корзина пуста
    add_to_cart_page.delete_item_from_cart("Ваш кошик порожній")
    
    # Закриваємо браузер
    #add_to_cart_page.close()   