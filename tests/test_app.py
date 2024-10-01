from playwright.sync_api import Page

from shiny.playwright import controller
from shiny.pytest import create_app_fixture
from shiny.run import ShinyAppProc

app = create_app_fixture("../app.py")


def test_app(page: Page, app: ShinyAppProc):
    page.goto(app.url)
    txt = controller.OutputText(page, "txt")
    slider = controller.InputSlider(page, "n")
    slider.set("55")
    txt.expect_value("n*2 is 110")

    check = controller.InputCheckboxGroup(page, "check")
    check.expect_choices(["A", "B", "C"])
    check.set(["A"])
