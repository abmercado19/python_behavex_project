from behave import step

from features.env_utils import get_app_url
from features.steps.pages.login_page import LoginPage


@step("I open the Tools QA page")
def open_main_page(context):
    app_url = get_app_url(context)
    context.execute_steps(
        """
            Given browser "{}"
            And I set browser size to 1400x900
        """.format(
            "Chrome"
        )
    )
    login_page = LoginPage(context.browser.driver, app_url)
    login_page.open_tools_qa_login_page()
    context.current_page = login_page
