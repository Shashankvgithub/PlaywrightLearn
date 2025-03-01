from .dashboard import DashboardPage


class LoginPage:

    def __init__(self,page):
        self.page=page

    # def navigate(self):
    #     self.page.goto("https://rahulshettyacademy.com/client/")

    def login(self,userEmail,password):
        self.page.locator("#userEmail").fill(userEmail)
        self.page.locator("#userPassword").fill(password)
        self.page.locator("#login").click()
        self.page.wait_for_selector(".fa-shopping-cart")
        dashboardpage=DashboardPage(self.page)
        return dashboardpage