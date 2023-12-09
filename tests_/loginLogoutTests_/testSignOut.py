from pages_.navigationBar_.navigationBar import NavigationBar
from tests_.baseTest import BaseTestWithLogin
from pages_.navigationBar_.accountListsDropDownPage import AccountListDropDownPage
from pages_.loginPage_.loginPage import LoginPage

class SignOut(BaseTestWithLogin):
    def test_sign_out(self):
        navigationBarObj = NavigationBar(self.simpleDriver)
        navigationBarObj.move_to_account_and_lists_button()
        accountListDropDownPageObj = AccountListDropDownPage(self.simpleDriver)
        accountListDropDownPageObj.click_to_sign_out_button()

        loginPageObj = LoginPage(self.simpleDriver)
        textOfSignIn = loginPageObj.get_sign_in_text()
        self.assertEqual(textOfSignIn, "Sign in")
