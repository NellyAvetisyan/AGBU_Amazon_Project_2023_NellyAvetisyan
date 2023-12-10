from pages_.basePage import BasePage
from selenium.webdriver.common.by import By


class SelectedProductDetailPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__addToCartButtonLocator = (By.ID, "add-to-cart-button")
        self.__selectedProductNameLocator = (By.ID, "title")
        self.__selectedProductPriceLocator = (By.XPATH, "(//span[@class='a-price a-text-price a-size-medium apexPriceToPay'])[1]")


    def click_add_to_cart_button(self):
        addToCartButtonElement = self._find_element(self.__addToCartButtonLocator)
        self._click(addToCartButtonElement)

    def get_selected_product_name_text(self):
        selectedProductNameText = self._find_element(self.__selectedProductNameLocator)
        return self._get_element_text(selectedProductNameText)

    def get_selected_product_price_text(self):
        selectedProductPriceText = self._find_element(self.__selectedProductPriceLocator)
        return self._get_element_text(selectedProductPriceText)