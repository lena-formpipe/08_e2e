# reguljära uttryck == regex
import re
from playwright.sync_api import Page, expect


def time_to_seconds(time_text: str) -> int:
    minutes, seconds = map(int, time_text.strip().split(":"))
    return minutes * 60 + seconds


def test_start_pause_reset_timer_countdown(page: Page, one_timer_widget):
    # hitta locator-knapparna i timer-widget
    start_button = one_timer_widget.get_by_role(
        "button").get_by_text(re.compile("Start", re.IGNORECASE))
    reset_button = one_timer_widget.get_by_role(
        "button").get_by_text(re.compile("reset", re.IGNORECASE))
    pause_button = one_timer_widget.get_by_role(
        "button").get_by_text(re.compile("paus", re.IGNORECASE))

    # hitta timerns startvärde(row time)
    first_time = one_timer_widget.locator(".row.time").inner_text()
    first_time_seconds = time_to_seconds(first_time)

    # verifiera synlighet knappar innan start
    expect(start_button).to_be_visible()
    expect(reset_button).to_be_visible()
    expect(pause_button).to_be_hidden()

    # starta timern och verifiera synlighet ändras efter start
    start_button.click()
    expect(start_button).to_be_hidden()
    expect(pause_button).to_be_visible()

    # nedräkning, vänta tills innehållet ändras och verifiera nedräkning
    page.wait_for_timeout(2000)
    second_time = one_timer_widget.locator(".row.time").inner_text()
    second_time_seconds = time_to_seconds(second_time)
    # assert används när man verifierar vanliga pythonvärden eller beräkningar
    # expect ska användas när man ska verifiera playwright-objekt
    assert second_time_seconds < first_time_seconds

    # pausa timern och verifiera synlighet på knappar ändrats efter paus
    pause_button.click()
    expect(start_button).to_be_visible()
    expect(pause_button).to_be_hidden()

    # reset timer och verifiera initiala värdet återställt
    reset_button.click()
    reset_time = one_timer_widget.locator(".row.time").inner_text()
    reset_time_seconds = time_to_seconds(reset_time)
    assert reset_time_seconds == first_time_seconds


def test_timer_count_up(page: Page, one_timer_widget_count_up):
    # hitta locator-knapparna i timer-widget
    start_button = one_timer_widget_count_up.get_by_role(
        "button").get_by_text(re.compile("Start", re.IGNORECASE))
    reset_button = one_timer_widget_count_up.get_by_role(
        "button").get_by_text(re.compile("reset", re.IGNORECASE))
    pause_button = one_timer_widget_count_up.get_by_role(
        "button").get_by_text(re.compile("paus", re.IGNORECASE))

    # hitta timerns startvärde(row time)
    first_time = one_timer_widget_count_up.locator(".row.time").inner_text()
    first_time_seconds = time_to_seconds(first_time)

    # verifiera synlighet knappar innan start
    expect(start_button).to_be_visible()
    expect(reset_button).to_be_visible()
    expect(pause_button).to_be_hidden()

    # starta timern och verifiera synlighet ändras efter start
    start_button.click()
    expect(start_button).to_be_hidden()
    expect(pause_button).to_be_visible()

    # uppräkning, vänta liten stund tills tiden ändrats
    page.wait_for_timeout(2000)
    second_time = one_timer_widget_count_up.locator(".row.time").inner_text()
    second_time_seconds = time_to_seconds(second_time)

    # assert används när man verifierar vanliga pythonvärden eller beräkningar
    # expect ska användas när man ska verifiera playwright-objekt
    assert second_time_seconds > first_time_seconds

    # pausa timern och verifiera synlighet på knappar ändrats efter paus
    pause_button.click()
    expect(start_button).to_be_visible()
    expect(pause_button).to_be_hidden()

    # reset timer och verifiera initiala värdet återställt
    reset_button.click()
    reset_time = one_timer_widget_count_up.locator(".row.time").inner_text()
    reset_time_seconds = time_to_seconds(reset_time)
    assert reset_time_seconds == first_time_seconds
