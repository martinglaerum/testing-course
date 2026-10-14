from playwright.sync_api import *
import re
import time

URL1 = "https://demoqa.com/text-box"
URL2 = "https://demoqa.com/checkbox"
URL3 = "https://demoqa.com/radio-button"
URL4 = "https://demoqa.com/webtables"
URL5 = "https://demoqa.com/buttons "
URL6 = "https://demoqa.com/links"

def test1():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        page = browser.new_page()
        page.goto(URL1)

        page.locator("#userName").fill("John Doe")
        page.locator("#userEmail").fill("does@gmail.com")
        page.locator("#currentAddress").fill("JupyterRoad 3")
        page.locator("#permanentAddress").fill("Nepture 14")

        expect(page.locator("#userName")).to_have_value("John Doe")
        expect(page.locator("#userEmail")).to_have_value("does@gmail.com")
        expect(page.locator("#currentAddress")).to_have_value("JupyterRoad 3")
        expect(page.locator("#permanentAddress")).to_have_value("Nepture 14")

        browser.close()

def test2():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        page = browser.new_page()
        page.goto(URL2)

        page.get_by_role("checkbox").check()
        expect(page.get_by_role("checkbox", name="Select Home")).to_have_attribute("aria-checked", "true")
        
        page.locator(".rc-tree-switcher").click()
        expect(page.locator("#result")).to_contain_text("home")
        expect(page.locator("#result")).to_contain_text("downloads")
        page.locator(".rc-tree-switcher").nth(1).click()
        page.get_by_role("checkbox").nth(0).uncheck()
        page.get_by_role("checkbox").nth(2).check()
        expect(page.locator("#result")).not_to_contain_text("home")

        browser.close()

def test3():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        page = browser.new_page()
        page.goto(URL3)

        expect(page.locator("#noRadio")).to_be_disabled()
        page.locator("#yesRadio").check()
        expect(page.locator("#yesRadio")).to_be_checked()

        expect(page.locator(".text-success")).to_contain_text("Yes")

        browser.close()

def test4():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        page = browser.new_page()
        page.goto(URL4)

        expect(page.locator("table")).to_contain_text("cierra@example.com")

        page.locator("#addNewRecordButton").click()  

        page.locator("#firstName").fill("John")
        page.locator("#lastName").fill("Doe")
        page.locator("#userEmail").fill("does@gmail.com")
        page.locator("#age").fill("24")
        page.locator("#salary").fill("41000")
        page.locator("#department").fill("HR")

        page.locator("#submit").click()
        expect(page.locator("table")).to_contain_text("does@gmail.com")

        browser.close()

def test5():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        page = browser.new_page()
        page.goto(URL5)

        page.locator("#doubleClickBtn").dblclick()
        expect(page.locator("#doubleClickMessage")).to_contain_text("You have done a double click")

        page.locator("#rightClickBtn").click(button="right")
        expect(page.locator("#rightClickMessage")).to_contain_text("You have done a right click")

        page.get_by_text("Click Me", exact=True).click()
        expect(page.locator("#dynamicClickMessage")).to_contain_text("You have done a dynamic click")        

        browser.close()

def test6():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        page = browser.new_page()
        page.goto(URL6)

        page.locator("#created").click()
        expect(page.locator("#linkResponse")).to_contain_text("201")

        page.locator("#no-content").click()
        expect(page.locator("#linkResponse")).to_contain_text("204")

        page.locator("#bad-request").click()
        expect(page.locator("#linkResponse")).to_contain_text("400")

        page.locator("#invalid-url").click()
        expect(page.locator("#linkResponse")).to_contain_text("404")

        browser.close()

test1()
test2()
test3()
test4()
test5()
test6()