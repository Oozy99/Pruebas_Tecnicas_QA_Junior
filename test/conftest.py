import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver():
    """
    fixture: es como una función de preparación.
    Se ejecuta ANTES de cada test, abre Chrome,
    y al terminar el test lo cierra automáticamente.
    """
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    driver.maximize_window()
    
    yield driver
    driver.quit()