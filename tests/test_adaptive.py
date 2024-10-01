from playwright.sync_api import Page

from shiny.playwright import controller
from shiny.pytest import create_app_fixture
from shiny.run import ShinyAppProc

app = create_app_fixture("../app-adaptive.py")


def test_app(page: Page, app: ShinyAppProc):
    page.goto(app.url)

    # below set of code work
    day = controller.InputCheckboxGroup(page, "adaptive-filter_day")
    day.expect_choice_labels(["Sun", "Fri"])
    day.expect_choices(["Sun", "Fri"])
    day.expect_selected([])

    day.set(["Fri"])
