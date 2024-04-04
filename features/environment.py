import os

from behavex_web.steps.web import *
from selenium import webdriver


def before_all(context):
    if all(
        env_var in os.environ for env_var in ["APP_URL", "USER_NAME", "USER_PASSWORD"]
    ):
        app_url = os.environ.get("APP_URL")
        user_name = os.environ.get("USER_NAME")
        user_password = os.environ.get("USER_PASSWORD")
        context.env_config = {
            "app_url": app_url,
            "user_name": user_name,
            "user_password": user_password,
        }
    else:
        raise Exception(
            "The following environment variables are required to execute the tests: "
            "APP_URL, USER_EMAIL and USER_PASSWORD"
        )
    context.execution_summary_filename = os.path.abspath(
        os.path.join(os.environ.get("OUTPUT"), "execution_summary.txt")
    )


def before_scenario(context, scenario):
    if "selected_browser" in context:
        if context.selected_browser == "chrome" and context.config.userdata.get(
            "headless_browser", None
        ):
            run_chrome_headless_mode(context)
        else:
            run_chrome_non_headless_mode(context)
            if (
                "options" in context.browser_args
                and "--headless" in context.browser_args["options"].arguments
            ):
                context.browser_args["options"].arguments.remove("--headless")
    print("-" * 40)
    print("Running Scenario: {}".format(scenario.name))
    print("-" * 40)


def before_step(context, step):
    """before_step behave hook"""
    logging.info("-" * 40)
    logging.info("STEP: {}".format(step.name))
    context.step = step


def after_scenario(context, scenario):
    with open(context.execution_summary_filename, "a+") as f:
        scenario_status = str(scenario.status).split(".")[-1]
        if (
            "MUTE" in scenario.tags
            and "MANUAL" not in scenario.tags
            and "WIP" not in scenario.tags
        ):
            # This is automated scenario that has been MUTED
            f.write(
                "MUTED_SCENARIO: {}: {}\n".format(scenario.feature.name, scenario.name)
            )
        if "MUTE" not in scenario.tags and "failed" in scenario_status:
            f.write(
                "FAILING_SCENARIO: {}: {}\n".format(
                    scenario.feature.name, scenario.name
                )
            )
        if scenario_status in ["passed", "failed"]:
            f.write(
                "EXECUTED_SCENARIO: {}: {}\n".format(
                    scenario.feature.name, scenario.name
                )
            )
            print("------------------------------------------")
            print(
                "Scenario Completed (Status: {}): {}".format(
                    scenario_status.upper(), scenario.name
                )
            )
            print("------------------------------------------")


def after_step(context, step):
    pass


# ####################################################################################################
# ########################################## HELPER METHODS ##########################################
# ####################################################################################################


def run_chrome_headless_mode(context):
    if "options" in context.browser_args:
        options = context.browser_args["options"]
    else:
        options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    disable_dev_shm_usage = context.config.userdata.get(
        "disable_dev_shm_usage", "false"
    )
    if disable_dev_shm_usage == "true":
        options.add_argument("--disable-dev-shm-usage")
    context.browser_args["options"] = options


def run_chrome_non_headless_mode(context):
    if "options" in context.browser_args:
        options = context.browser_args["options"]
    else:
        options = webdriver.ChromeOptions()
    disable_dev_shm_usage = context.config.userdata.get(
        "disable_dev_shm_usage", "false"
    )
    if disable_dev_shm_usage == "true":
        options.add_argument("--disable-dev-shm-usage")
    context.browser_args["options"] = options
