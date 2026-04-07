import pytest
from pages.login import login

EMAIL = "cozemik9204@kancwut.my.id"
PASWORD = "laaurora9"
CREDENCILES_INVALIDAS = "NO EXISTE"

def test_login_prueba(driver):
    login_pagina = login(driver)
    assert login_pagina.URL == "https://sauce-demo.myshopify.com/account/login"
    print("URL es correcta")

