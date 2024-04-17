"""
This module contains the definition of common steps used by the BDD tests in the project
"""

import logging

from behave import step
from behaving.web.steps import *

from features.env_utils import get_app_url
from features.steps.pages.login_page import LoginPage


@step(u'I open the Tools QA page')
def open_main_page(context):
    """Initializes the browser and opens the Tools QA Login page"""
    app_url = get_app_url(context)
    context.execute_steps(
        """
            Given browser "{}"
            And I set browser size to 1400x900
        """.format(
            context.default_browser))
    login_page = LoginPage(context.browser.driver, app_url)
    login_page.open_tools_qa_login_page()
    context.current_page = login_page


@step(u'I set browser size to {size}')
def set_browser_window_size(context, size):
    """Set browser to the specified screen resolution"""
    split_size = size.split('x')
    for browser_selected in context.browsers.values():
        browser_selected.driver.set_window_size(split_size[0], split_size[1])
        logging.info('Browser size has been changed to {0}x{1}'.format(split_size[0], split_size[1]))
