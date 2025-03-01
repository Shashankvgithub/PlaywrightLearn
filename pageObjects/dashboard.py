from .orderHistory import OrderHistoryPage


class DashboardPage:

    def __init__(self,page):
        self.page=page

    def selectOrdersNavLink(self):
        self.page.get_by_text("ORDERS").click()
        orderHistoryPage=OrderHistoryPage(self.page)
        return orderHistoryPage