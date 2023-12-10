from pages_.navigationBar_.navigationBar import NavigationBar
from pages_.navigationBar_.cartPage import CartPage
from tests_.baseTest import BaseTestWithLogin

class DeletionFromCartPage(BaseTestWithLogin):
    def test_emptiness_of_cart_page(self):
        navigationBarObj = NavigationBar(self.simpleDriver)
        navigationBarObj.click_to_cart_button()
        cartPageObj = CartPage(self.simpleDriver)
        emptyCartMessage = cartPageObj.get_text_of_empty_cart_message()

        self.assertEqual(emptyCartMessage, "Your Amazon Cart is empty.")
        print("Warning! The Cart Is Empty!")

    def test_delete_first_product_from_cart(self):
        navigationBarObj = NavigationBar(self.simpleDriver)
        navigationBarObj.click_to_cart_button()
        cartPageObj = CartPage(self.simpleDriver)
        cartCountNumberBeforeDeletion = cartPageObj.get_cart_count()
        cartPageObj.delete_first_product_from_cart()
        cartCountNumberAfterDeletion = cartPageObj.get_cart_count()

        self.assertEqual(cartCountNumberAfterDeletion, cartCountNumberBeforeDeletion - 1)

    def test_delete_all_products_from_cart(self):
        navigationBarObj = NavigationBar(self.simpleDriver)
        navigationBarObj.click_to_cart_button()
        cartPageObj = CartPage(self.simpleDriver)
        cartPageObj.delete_all_products_from_cart()
        cartCountNumber = cartPageObj.get_cart_count()

        self.assertEqual(cartCountNumber, 0)

