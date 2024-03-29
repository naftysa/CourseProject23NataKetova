import pytest
from modules.common.database import Database



@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name("Sergii")

    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    waner_qnt = db.select_product_qnt_by_id(1)

    assert waner_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(1, "вода солодка", "з цукром", 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_order_insert():
    db = Database()
    db.insert_order(3, 3, 2, '14:28:26')
    customer_id_added = db.get_detailed_orders()
    
    print("Customer_id row added to db is: ", customer_id_added)
    print()
    

@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, "тестові", "дані", 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database 
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Zamovlennya", orders)
    # Check quantity of orders equal to 1
    assert len(orders) == 2

    # Check structure of data
    assert orders[0][0] == 1
    assert orders[0][1] == "Sergii"
    assert orders[0][2] == "вода солодка"
    assert orders[0][3] == "з цукром"


@pytest.mark.database
def test_cannot_insert_text_to_int_column():
    db = Database()
    db.insert_product("88", "test data", "description of test data", "true")
    check_id = db.get_detailed_orders()
    print("Check added values: ", check_id)
    
    
