from pages_.basePage import BasePage
from selenium.webdriver.common.by import By


class SearchResultPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__searchResultFirstProductLocator = (By.XPATH, "(//div[@class='sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20'])[1]")
        self.__firstProductNameTextLocator = (By.XPATH, "(//span[@class='a-size-base-plus a-color-base a-text-normal'])[1]")
        self.__productPriceLocator = (By.XPATH, "(//span[@class='a-offscreen'])[8]")

    def click_to_first_product(self):
        searchResultFirstProductElement = self._find_element(self.__searchResultFirstProductLocator)
        self._click(searchResultFirstProductElement)

    def get_text_of_first_product_name(self):
        textOfFirstProductNameElement = self._find_element(self.__firstProductNameTextLocator)
        return self._get_element_text(textOfFirstProductNameElement)

    def get_text_of_first_product_price(self):
        textOfFirstProductPrice = self._find_element(self.__productPriceLocator)
        return self._get_element_text(textOfFirstProductPrice)
