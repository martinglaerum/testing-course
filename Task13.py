from playwright.sync_api import *
import time


URL = "https://demoqa.com/automation-practice-form"


def test1():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        page = browser.new_page()
        page.goto(URL)

        page.locator("#firstName").fill("John")
        page.locator("#lastName").fill("Doe")
        page.locator("#gender-radio-1").check()
        page.locator("#userEmail").fill("does@gmail.com")
        page.locator("#userNumber").fill("1918171615")
        page.locator("#subjectsInput").fill("ma")
        page.locator("#subjectsInput").press("Tab")
        page.locator("#subjectsInput").fill("hin")
        page.locator("#subjectsInput").press("Tab")

        page.locator("#hobbies-checkbox-3").check()
        page.locator("#hobbies-checkbox-1").check()
        page.locator("#currentAddress").fill("JupyterRoad 3")

        page.locator("#react-select-3-input").fill("U")
        page.locator("#react-select-3-input").press("Tab")

        page.locator("#react-select-4-input").fill("C")
        page.locator("#react-select-4-input").press("Tab")

        page.locator("#uploadPicture").set_input_files({
                "name": "profile.png",
                "mimeType": "image/png",
                "buffer": b"Hello Image"
            }
        )

        page.locator("#dateOfBirthInput").click()
        page.locator(".react-datepicker__month-select").select_option("1")
        page.locator(".react-datepicker__year-select").select_option("2001")
        page.locator(".react-datepicker__day--008:not(.react-datepicker__day--outside-month)").click()

        page.locator("#submit").click()

        expect(page.locator(".modal-body")).to_contain_text("does@gmail.com")
        expect(page.locator(".modal-body")).to_contain_text("1918171615")
        expect(page.locator(".modal-body")).to_contain_text("February")
        expect(page.locator(".modal-body")).to_contain_text("Math")
        expect(page.locator(".modal-body")).to_contain_text("Hindi")

        browser.close()

test1()