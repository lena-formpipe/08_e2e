# reguljära uttryck == regex
import re
import pytest
from playwright.sync_api import Page


@pytest.fixture()
def url():
    base_url = "https://lejonmanen.github.io/timer-vue/"
    return base_url


@pytest.fixture()
def one_timer_widget(page: Page, url):
    page.goto(url)

    # hitta knappen add timer och lägg till en timer-widget
    button_locator = page.get_by_role("button")
    button_first = button_locator.get_by_text(
        re.compile("timer", re.IGNORECASE))
    button_first.click()

    # hitta den nedersta widgeten, finns en skräp-widgeten på sidan
    timer_widget = page.locator(".widget").last

    return timer_widget


@pytest.fixture()
def one_timer_widget_count_up(page: Page, url, one_timer_widget):

    # klicka på settings för att öppna inställningar
    one_timer_widget.locator(".icon.settings").click()
    direction = one_timer_widget.locator(".settings-menu").get_by_text(
        re.compile("counting down", re.IGNORECASE))
    on_off = direction.locator(".on-off")
    on_off.click()

    return one_timer_widget


@pytest.fixture()
def one_notes_widget(page: Page, url):
    page.goto(url)

    # hitta knappen add timer och lägg till en timer-widget
    button_locator = page.get_by_role("button")
    button_first = button_locator.get_by_text(
        re.compile("add note", re.IGNORECASE))
    button_first.click()

    # hitta den nedersta widgeten
    notes_widget = page.locator(".widget").last

    return notes_widget
