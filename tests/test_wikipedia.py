import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import have, be
from selene.support.shared import browser
from allure_commons.types import Severity
from allure import step

from python_wikipedia_mobile.model import app


@allure.tag("ui", "mobile")
@allure.label('owner', 'vkamenskiy')
@allure.feature('UI')
@allure.story('Search')
@allure.severity(Severity.NORMAL)
@allure.title('Search python')
def test_search_python():
    with step('Skip onboarding'):
        app.given_opened()

    with step("Search Python"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type(
            "Python"
        )

    with step("Verify content found"):
        browser.all(
            (AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")
        ).filtered_by(have.text("Python (programming language)")).should(
            have.size_greater_than(0)
        )


@allure.tag("ui", "mobile")
@allure.label('owner', 'vkamenskiy')
@allure.feature('UI')
@allure.story('Search')
@allure.severity(Severity.NORMAL)
@allure.title('Search history saved')
def test_search_history_saved():
    with step('Skip onboarding'):
        app.given_opened()

    with step("Search Python"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type(
            "Python"
        )
        browser.all(
            (AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")
        ).element_by(have.text("Python (programming language)")).click()

    with step('Checking the search results saving'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Navigate up")).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Navigate up")).click()
        browser.all(
            (AppiumBy.ID, "org.wikipedia.alpha:id/navigation_bar_item_small_label_view")
        ).element_by(have.text("Search")).click()
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")
        ).should(have.text("Python (programming language)"))


@allure.tag("ui", "mobile")
@allure.label('owner', 'vkamenskiy')
@allure.feature('UI')
@allure.story('Onboarding')
@allure.severity(Severity.TRIVIAL)
@allure.title('Headers on onboarding screen')
def test_headers_on_onboarding_screen():
    with step("First page header"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(
            have.text("The Free Encyclopedia\n…in over 300 languages")
        )
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")
        ).click()

    with step("Second page header"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(
            have.text("New ways to explore")
        )
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")
        ).click()

    with step("Third page header"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(
            have.text("Reading lists with sync")
        )
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")
        ).click()

    with step("Fourth page header"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(
            have.text("Send anonymous data")
        )


@allure.tag("ui", "mobile")
@allure.label('owner', 'vkamenskiy')
@allure.feature('UI')
@allure.story('Language')
@allure.severity(Severity.NORMAL)
@allure.title('Add Russian language')
def test_add_russian_language():
    with step('Open add language page'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/addLangContainer")).click()

    with step('Add Russian language'):
        browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/wiki_language_title")).element_by(
            have.text("ADD LANGUAGE")
        ).click()
    browser.all(
            (AppiumBy.ID, "org.wikipedia.alpha:id/localized_language_name")
        ).element_by(have.text("Русский")).click()

    with step('Check that the Russian language is added'):
        browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/wiki_language_title")).element_by(
            have.text("Русский")
        ).should(be.visible)


@allure.tag("ui", "mobile")
@allure.label('owner', 'vkamenskiy')
@allure.feature('UI')
@allure.story('Language')
@allure.severity(Severity.NORMAL)
@allure.title('Delete added language')
def test_delete_added_language():
    with step('Open add language page'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/addLangContainer")).click()

    with step('Add Russian language'):
        browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/wiki_language_title")).element_by(
            have.text("ADD LANGUAGE")
        ).click()
        browser.all(
            (AppiumBy.ID, "org.wikipedia.alpha:id/localized_language_name")
        ).element_by(have.text("Русский")).click()

    with step('Delete Russian language'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "More options")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/title")).click()
        browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/wiki_language_title")).element_by(
            have.text("Русский")
        ).click()
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/menu_delete_selected")
        ).click()
        browser.element((AppiumBy.ID, "android:id/button1")).click()

    with step('Check that the Russian language is deleted'):
        browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/wiki_language_title")).element_by(
            have.no.text("Русский")
        )
