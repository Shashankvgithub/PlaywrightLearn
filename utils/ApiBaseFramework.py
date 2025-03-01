from playwright.sync_api import Playwright

# login_Payload={'userEmail':'rahulshetty@gmail.com','userPassword':'Iamking@000'}
order_PayLoad={"orders":[{"country":"India","productOrderedId":"67a8dde5c0d3e6622a297cc8"}]}
class APIUtilities:

    def LoginAPI(self,playwright:Playwright,test_user_credential):
        user_email = test_user_credential['userEmail']
        user_password=test_user_credential['password']
        api = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        loginresponse = api.post("/api/ecom/auth/login", data={'userEmail':user_email,'userPassword':user_password})
        logintoken = loginresponse.json()["token"]
        return logintoken

    def CreateOrder(self,playwright:Playwright,test_user_credential):
        token=self.LoginAPI(playwright,test_user_credential)

        createAPI=playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        orderResponse=createAPI.post("/api/ecom/order/create-order",data=order_PayLoad,headers={"Authorization":f"{token}"})
        return orderResponse.json()["orders"][0]
