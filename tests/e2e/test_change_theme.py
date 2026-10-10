# reguljära uttryck == regex
import re
import pytest
from playwright.sync_api import Page, expect

THEMES = [
    ("orange", "#D6961E", "#E1B972"),
    ("dark", "#1189AF", "#141414"),
    ("forest", "#6DB86D", "#064806"),
    ("christmas", "#187f42", "#165b33")
]


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return f"rgb({r}, {g}, {b})"


@pytest.mark.parametrize("theme_chosen, start_button_color, "
                         "background_color", THEMES,)
def test_theme_parametrized(
        page: Page, url, one_timer_widget, theme_chosen,
        start_button_color, background_color,):
    # klicka på rätt tema och identifiera start_knappen
    theme_button = page.get_by_role(
        "button").get_by_text(re.compile(theme_chosen, re.IGNORECASE))
    theme_button.click()
    start_button = one_timer_widget.get_by_role(
        "button").get_by_text(re.compile("Start", re.IGNORECASE))

    expect(start_button).to_have_css(
        "background-color",
        hex_to_rgb(start_button_color)
    )

    expect(page.locator("body")).to_have_css(
        "background-color",
        hex_to_rgb(background_color)
    )
