from selenium.webdriver.common.by import By


class login:
    URL = "https://sauce-demo.myshopify.com/account/login"
    CAMPO_EMAIL = (By.XPATH, "//input[@id='customer_email']")
    CAMPO_PASSWORD = (By.XPATH, "//input[@id='customer_password']")
    BOTON_SINGIN = (By.XPATH, "button[name='commit']")
    MENSAJE_ERROR = (By.XPATH, ".notice--error")  # clase del mensaje de error

    def __init__(self, driver):
        self.driver = driver

    def abrir_pagina(self):
        self.driver.get(self.URL)