from playwright.sync_api import *
import re
import time

URL = "https://www.saucedemo.com/"


def log_in_test(username, password):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False, slow_mo=300)
            page = browser.new_page()
            page.goto(URL)

            page.locator("#user-name").fill("username")
            page.locator("#password").fill("secret_sauce2")
            page.locator("#login-button").click()
            expect(page.get_by_role("alert")).to_have_text("Epic sadface: Username and password do not match any user in this service")

            page.locator("#user-name").fill(username)
            page.locator("#password").fill("")
            page.locator("#login-button").click()
            expect(page.get_by_role("alert")).to_have_text("Epic sadface: Password is required")

            page.locator("#user-name").fill(username)
            page.locator("#password").fill(password)
            page.locator("#login-button").click()
            expect(page.locator(".title")).to_contain_text("Products")

            browser.close()
            return True
    except:
        print(f"User {username} was not able to log in")
        return False

def main_page_test(username, password):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False, slow_mo=300)
            page = browser.new_page()
            page.goto(URL)

            page.locator("#user-name").fill(username)
            page.locator("#password").fill(password)
            page.locator("#login-button").click()
            expect(page.locator(".title")).to_contain_text("Products")

            page.locator(".inventory_item_name").nth(0).click()
            expect(page.locator(".inventory_details_desc")).to_have_text(
                "carry.allTheThings() with the sleek, streamlined Sly Pack " \
                "that melds uncompromising style with unequaled laptop and tablet protection."
            )

            expect(page.locator(".inventory_details_price")).to_contain_text("29.99")
            expect(page.locator("body")).not_to_contain_text("Bike Light")
            page.locator("#back-to-products").click()


            page.locator(".product_sort_container").select_option("Price (low to high)")
            expect(page.locator(".inventory_item_name").nth(0)).to_have_text("Sauce Labs Onesie")
            expect(page.locator(".inventory_item_price").nth(0)).to_contain_text("7.99")

            page.locator(".product_sort_container").select_option("Name (Z to A)")
            expect(page.locator(".inventory_item_name").nth(0)).to_have_text("Test.allTheThings() T-Shirt (Red)")
            expect(page.locator(".inventory_item_price").nth(0)).to_contain_text("15.99")

            browser.close()
            return True
    except:
        print(f"User {username} was not use the main page properly")
        return False

def cart_test(username, password):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False, slow_mo=300)
            page = browser.new_page()
            page.goto(URL)

            page.locator("#user-name").fill(username)
            page.locator("#password").fill(password)
            page.locator("#login-button").click()
            expect(page.locator(".title")).to_contain_text("Products")

            page.locator("#add-to-cart-sauce-labs-backpack").click()
            page.locator("#add-to-cart-sauce-labs-bolt-t-shirt").click()
            page.locator("#add-to-cart-sauce-labs-fleece-jacket").click()
            page.locator("#add-to-cart-sauce-labs-bike-light").click()
            page.locator("#remove-sauce-labs-fleece-jacket").click()
            page.locator("#remove-sauce-labs-bolt-t-shirt").click()
            page.locator(".shopping_cart_link").click()

            expect(page.locator("#cart_contents_container").nth(0)).to_contain_text("Sauce Labs Backpack")
            expect(page.locator("#cart_contents_container").nth(0)).to_contain_text("Sauce Labs Bike Light")
            expect(page.locator("#cart_contents_container").nth(0)).not_to_contain_text("Sauce Labs Fleece Jacket")
            page.locator("#remove-sauce-labs-backpack").click()
            expect(page.locator("#cart_contents_container").nth(0)).not_to_contain_text("Sauce Labs Backpack")

            browser.close()
            return True
    except:
        print(f"User {username} can not use the cart")
        return False


def checkout_test(username, password):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False, slow_mo=300)
            page = browser.new_page()
            page.goto(URL)

            page.locator("#user-name").fill(username)
            page.locator("#password").fill(password)
            page.locator("#login-button").click()
            page.locator("#add-to-cart-sauce-labs-backpack").click()
            page.locator(".shopping_cart_link").click()
            page.locator("#checkout").click()

            page.locator("#first-name").fill("John")
            page.locator("#continue").click()
            expect(page.locator(".error-message-container")).to_contain_text("Error: Last Name is required")
            
            page.locator("#last-name").fill("Doe")
            page.locator("#continue").click()
            expect(page.locator(".error-message-container")).to_contain_text("Error: Postal Code is required")


            page.locator("#last-name").fill("")
            page.locator("#postal-code").fill("1881")  
            page.locator("#continue").click()
            expect(page.locator(".error-message-container")).to_contain_text("Error: Last Name is required")

            page.locator("#last-name").fill("Doe")
            page.locator("#first-name").fill("")  
            page.locator("#continue").click()
            expect(page.locator(".error-message-container")).to_contain_text("Error: First Name is required")

            

            page.locator("#first-name").fill("John")
            page.locator("#continue").click()
            expect(page.locator(".title")).to_contain_text("Checkout: Overview")

            browser.close()

            return True
    except:
        print(f"User {username} can not check out")
        return False

def confirm_order_test(username, password):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False, slow_mo=300)
            page = browser.new_page()
            page.goto(URL)
            
            page.locator("#user-name").fill(username)
            page.locator("#password").fill(password)
            page.locator("#login-button").click()
            page.locator("#add-to-cart-sauce-labs-backpack").click()
            page.locator(".shopping_cart_link").click()
            page.locator("#checkout").click()
            page.locator("#first-name").fill("John")
            page.locator("#last-name").fill("Doe")
            page.locator("#postal-code").fill("1881")
            page.locator("#continue").click()

            expect(page.locator(".title")).to_contain_text("Checkout: Overview")
            expect(page.locator(".inventory_item_name")).to_contain_text("Sauce Labs Backpack")
            expect(page.locator(".inventory_item_price")).to_contain_text("29.99")
            expect(page.locator(".summary_total_label")).to_contain_text("32.39")

            page.locator("#finish").click()
            expect(page.locator(".title")).to_contain_text("Checkout: Complete")

            browser.close()
            return True
    except:
        print(f"User {username} confirm their order")
        return False


def main():
    start_time = time.time()
    users = ["standard_user","locked_out_user","problem_user",
        "performance_glitch_user","error_user","visual_user"
    ]

    password = "secret_sauce"

    for user in users:
        print(f"\n## NOW TESTING USER: {user} ##")
        success = True

        if log_in_test(user, password):
            result = main_page_test(user, password)
            success = success and result
            result = cart_test(user, password)
            success = success and result
            result = checkout_test(user, password)
            success = success and result
            result = confirm_order_test(user, password)
            success = success and result
        else:
            success = False

        if success:
            print("✅ SUCCESS!")
        else:
            print("❌ hmmm... this isnt good")

    end_time = time.time()
    print(f"Program took {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()