import pytest
import selene
from selene.support.shared import browser
from selene import be, have


@pytest.fixture
def browser_open():
    browser.open('https://google.com')
    browser.driver.set_window_size(1024, 768)

def test_google_successfull(browser_open):

    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_google_unsuccessfull(browser_open):

    browser.element('[name="q"]').should(be.blank).type('dkjfvndkjfn').press_enter()
    assert ('[id="search"]') == ('Selene - User-oriented Web UI browser tests in Python')
    print('Результатов нет')