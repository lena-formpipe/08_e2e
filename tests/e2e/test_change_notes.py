# reguljära uttryck == regex
import re
from playwright.sync_api import Page, expect


def test_change_notes(page: Page, one_notes_widget):
    new_text = "Lorem ipsum dolor."
    # leta upp heading h3 och klicka på den
    heading_notes = one_notes_widget.get_by_role("heading").get_by_text(
        re.compile("change text", re.IGNORECASE)
    )
    heading_notes.click()
    text_input = one_notes_widget.locator("input")
    text_input.fill(new_text)
    text_input.press("Enter")

    # hitta elementet med nya texten
    heading_notes_new_text = one_notes_widget.get_by_role(
        "heading").get_by_text(new_text)
    expect(heading_notes_new_text).to_be_visible()
