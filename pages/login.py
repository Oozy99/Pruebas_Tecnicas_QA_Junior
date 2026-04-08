from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class login:
    URL = "https://sauce-demo.myshopify.com/account/login"
    URL_ACCOUNT = "https://sauce-demo.myshopify.com/account"
    URL_HOME = "https://sauce-demo.myshopify.com/"

    CAMPO_EMAIL = (By.XPATH, "//input[@id='customer_email']")
    CAMPO_PASSWORD = (By.XPATH, "//input[@id='customer_password']")
    BOTON_SINGIN = (By.XPATH, "//input[@value='Sign In']")
    MENSAJE_ERROR = (By.XPATH, "//div[contains(@class,'notice--error')] | //ul[contains(@class,'errors')]")
    LOGO_SAUCE_DEMO = (By.XPATH, "//img[contains(@src,'logo.png')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir_pagina(self):
        self.driver.get(self.URL)
    
    def ingresar_email(self, email):
        campo = self.wait.until(EC.visibility_of_element_located(self.CAMPO_EMAIL))
        campo.send_keys(email)
 
    def ingresar_password(self, password):
        campo = self.wait.until(EC.visibility_of_element_located(self.CAMPO_PASSWORD))
        campo.send_keys(password)
 
    def clic_singin(self):
        boton = self.wait.until(EC.element_to_be_clickable(self.BOTON_SINGIN))
        boton.click()
 
    def clic_logo(self):
        logo = self.wait.until(EC.element_to_be_clickable(self.LOGO_SAUCE_DEMO))
        logo.click()
 
    def mensaje_error_visible(self):
        try:
            elemento = self.wait.until(EC.visibility_of_element_located(self.MENSAJE_ERROR))
            return elemento.is_displayed()
        except Exception:
            return False
 
    def url_actual(self):
        return self.driver.current_url
 
    def esperar_redireccion_account(self):
        try:
            self.wait.until(EC.url_contains("/account"))
            return True
        except Exception:
            return False
 
    def esperar_redireccion_home(self):
        try:
            self.wait.until(EC.url_to_be(self.URL_HOME))
            return True
        except Exception:
            return False
 
    def logo_visible(self):
        try:
            elemento = self.wait.until(EC.visibility_of_element_located(self.LOGO_SAUCE_DEMO))
            return elemento.is_displayed()
        except Exception:
            return False