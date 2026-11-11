from playwright.sync_api import sync_playwright

link = input("Enter The Link: ")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(link)
    page.screenshot(path="demoinput.png")
    browser.close()