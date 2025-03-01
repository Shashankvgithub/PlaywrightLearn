
# pytest .\test_web_api.py --tracing on --headed --url https://rahulshettyacademy.com/client --browser firefox

import json
import time

import pytest
from playwright.sync_api import Playwright, expect, Page

from pageObjects.dashboard import DashboardPage
from pageObjects.login import LoginPage
from utils.ApiBaseFramework import APIUtilities

# json file -->Utils -->Access into test
with open("data/credentials.json") as f:
    test_data = json.load(f)
    user_credentials_list = test_data["user_credentials"]

@pytest.mark.parametrize("test_user_credential",user_credentials_list)
def test_WebtoAPI(playwright:Playwright,browserInstance,test_user_credential):

    userEmail=test_user_credential["userEmail"]
    password=test_user_credential["password"]

    #Create an Order using API
    apiUtils = APIUtilities()
    orderID = apiUtils.CreateOrder(playwright,test_user_credential)

    loginPage=LoginPage(browserInstance)
    dashboardPage=loginPage.login(userEmail,password)
    orderHistoryPage=dashboardPage.selectOrdersNavLink()
    orderDetailsPage=orderHistoryPage.selectOrder(orderID)
    orderDetailsPage.verifyOrderMessage()

def test_firstrun(browserInstance):
    browserInstance.goto("https://google.com")

# def test_GetApi(playwright:Playwright):
#     apirequest=playwright.request.new_context(base_url="https://catfact.ninja")
#     apires=apirequest.get("/fact")
#     print(apires.json())

def test_SecondRun(browserInstance):
    browserInstance.goto("https://msn.com")