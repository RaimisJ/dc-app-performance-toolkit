from selenium.webdriver.common.by import By
from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from util.conf import JIRA_SETTINGS

def app_specific_action_sr(webdriver, datasets):
    page = BasePage(webdriver)

    report_url = "/plugins/servlet/simple-reports-app/reports"
    iframe_id = "simple-reports-iframe"

    @print_timing("selenium_app_custom_action")
    def measure():

        @print_timing("selenium_app_custom_action:view_report")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}{report_url}")
            page.wait_until_available_to_switch((By.ID, iframe_id)) # switch to app iframe
            page.wait_until_visible((By.CLASS_NAME , "centered")) # loading started and spinner is visible
            page.wait_until_invisible((By.CLASS_NAME , "centered")) # loading finished and spinner is not visible
        sub_measure()
    measure()

def app_specific_action_dashboard(webdriver, datasets):
    page = BasePage(webdriver)

    report_url = "/secure/Dashboard.jspa?selectPageId=10100"
    iframe_id = "dashboard-item-iframe"

    @print_timing("selenium_app_custom_action")
    def measure():

        @print_timing("selenium_app_custom_action:view_report")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}{report_url}")
            page.wait_until_available_to_switch((By.ID, iframe_id)) # switch to app iframe
            page.wait_until_visible((By.CLASS_NAME , "centered")) # loading started and spinner is visible
            page.wait_until_invisible((By.CLASS_NAME , "centered")) # loading finished and spinner is not visible
        sub_measure()
    measure()
