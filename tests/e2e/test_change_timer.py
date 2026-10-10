# reguljära uttryck == regex
import re
from playwright.sync_api import Page, expect


def test_change_timer(page: Page, url, one_timer_widget):
    # verifiera att standardtiden är 15:00
    # skriv ut time i kommandoraden med -s om du vill verifiera
    time = one_timer_widget.locator(".row.time")
    expect(time).to_have_text(re.compile("15:00"))
    print("Tiden är:", time.inner_text())

    # klicka på settings för att öppna inställningar
    settings_button = one_timer_widget.locator(".icon.settings")
    settings_button.click()

    # verifiera synlig textbox med class .settings.menu för att ändra tiden.
    textbox_locator = one_timer_widget.locator(
        ".settings-menu").get_by_role("textbox")
    expect(textbox_locator).to_be_visible()

    # ändra tiden till 1 och stäng rutan för inställningar,
    # verifiera att settings-menu inte är synlig längre
    textbox_locator.fill("1")
    settings_button.click()
    expect(textbox_locator).to_be_hidden()

    # klicka på reset för att uppdatera till nya tiden,
    # re.compile och re.IGNORECASE gör testet mindre flaky
    one_timer_widget.get_by_role("button").get_by_text(re.compile(
        "reset", re.IGNORECASE)).click()

    # kontrollera att tiden nu är 1:00
    # med re.compile behöver man inte verifiera exakta siffror,
    # mindre flaky att även acceptera 1:00
    new_time = one_timer_widget.locator(".row.time")
    expect(new_time).to_have_text(re.compile("1:00"))
    # skriv ut time i kommandoraden med -s om du vill verifiera
    print("Tiden är:", new_time.inner_text())
