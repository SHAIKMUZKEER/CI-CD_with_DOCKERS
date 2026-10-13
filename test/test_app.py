
from pathlib import Path

from playwright.sync_api import sync_playwright

PROJECT_DIR = Path(__file__).resolve().parents[1]
FRONTEND_DIR = PROJECT_DIR / "src"


def test_frontend_files_exist():
    assert (FRONTEND_DIR / "index.html").exists()
    assert (FRONTEND_DIR / "script.js").exists()
    assert (FRONTEND_DIR / "style.css").exists()


def test_frontend_loads_and_generates_table():
    html_file = FRONTEND_DIR / "index.html"

    with sync_playwright() as p:
        browser = p.chromium.launch()

        try:
            page = browser.new_page()

            # Open the HTML file directly
            page.goto(html_file.as_uri())

            # Check page title
            assert "Multiply" in page.title()

            # Check input and button
            assert page.locator("#number").count() == 1
            assert page.locator("#generateBtn").count() == 1

            # Check CSS and JavaScript links
            assert page.locator(
                'link[rel="stylesheet"][href="style.css"]'
            ).count() == 1

            assert page.locator(
                'script[src="script.js"]'
            ).count() == 1

            # Enter number and generate table
            page.locator("#number").fill("7")
            page.locator("#generateBtn").click()

            # Verify 10 result cards
            cards = page.locator(".table-card")
            assert cards.count() == 10

            # Verify first multiplication row
            first_card = cards.nth(0)

            assert first_card.locator(
                ".equation"
            ).inner_text() == "7 × 1 ="

            assert first_card.locator(
                ".answer"
            ).inner_text() == "7"

            # Verify last multiplication row
            last_card = cards.nth(9)

            assert last_card.locator(
                ".equation"
            ).inner_text() == "7 × 10 ="

            assert last_card.locator(
                ".answer"
            ).inner_text() == "70"

        finally:
            browser.close()
