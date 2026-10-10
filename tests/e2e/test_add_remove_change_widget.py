# reguljära uttryck == regex
import re
from playwright.sync_api import Page, expect


def test_add_remove_change_widget(page: Page, url):
    page.goto(url)

    # hitta knappen add timer och lägg till en timer-widget
    button_locator = page.get_by_role("button")
    button_first = button_locator.get_by_text(re.compile(
        "timer", re.IGNORECASE))
    button_first.click()

    # leta upp heading h3 och kontrollera att den är synlig
    # här kontrolleras inte vilken ordning, bara att det finns
    heading_timer = page.get_by_role("heading").get_by_text(
        re.compile("Break", re.IGNORECASE))
    expect(heading_timer).to_be_visible()

    # hitta knappen add notes och lägg till en notes-widget
    # fast gör allt-i-ett-svep
    page.get_by_role("button").get_by_text(
        re.compile("note", re.IGNORECASE)).click()

    # leta upp heading h3 och kontrollera att den är synlig
    # här kontrolleras inte vilken ordning, bara att det finns
    heading_note = page.get_by_role(
        "heading").get_by_text(re.compile("change text", re.IGNORECASE))
    expect(heading_note).to_be_visible()

    # hitta den nedersta widgeten och klicka på "pil upp"
    # pil upp är inte en button, använd class .widget och class .icon.up
    bottom_widget_1 = page.locator(".widget").last
    bottom_widget_1.locator(".icon.up").click()

    # verifiera att widgetarna bytt ordning
    bottom_widget_2 = page.locator(".widget").last
    expect(bottom_widget_2.get_by_role("heading").get_by_text(
        re.compile("Break", re.IGNORECASE))).to_be_visible()

    # hitta den nedersta widgeten och klicka på "soptunna"
    # utgå från class .widget och class .icon.close
    bottom_widget_3 = page.locator(".widget").last
    bottom_widget_3.locator(".icon.close").click()

    # hitta den nya nedersta widgeten och klicka på "soptunna"
    # utgå från class .widget och class .icon.close
    bottom_widget_4 = page.locator(".widget").last
    bottom_widget_4.locator(".icon.close").click()

    # OBS! Även om båda widgets är borta så finns den spök-widget utan h3
    # måste filtrera fram widgets som har h3, och se till att de har count(0)
    widgets_with_h3 = page.locator(".widget").filter(has=page.locator("h3"))
    expect(widgets_with_h3).to_have_count(0)
