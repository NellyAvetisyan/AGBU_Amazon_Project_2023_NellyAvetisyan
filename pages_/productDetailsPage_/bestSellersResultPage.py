from pages_.basePage import BasePage
from selenium.webdriver.common.by import By


class BestSellersResultPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.__bestSellersFirstProductLocator = (By.XPATH, "(//li[@class ='a-carousel-card'])[1]")

    def click_to_first_product(self):
        bestSellersFirstProductElement = self._find_element(self.__bestSellersFirstProductLocator)
        self._click(bestSellersFirstProductElement)
