import pytest
from pages.login import login
 
EMAIL = "cozemik9204@kancwut.my.id"
PASWORD = "laaurora9"
CREDENCILES_INVALIDAS = "correoNoexiste@gmail.com"
 
 
# ──────────────────────────────────────────
# TC-01: Login Exitoso
# ──────────────────────────────────────────
def test_login_exitoso(driver):
    """
    Pasos:
        1. Ingresar al portal de inicio
        2. Ingresar usuario y contraseña validos
        3. Clic en Iniciar Sesion (SIGN IN)
    Resultado esperado:
        Redirige a /account, el logo es visible,
        al dar clic en el logo lleva a la pagina con productos
    """
    login_pagina = login(driver)
    login_pagina.abrir_pagina()
    login_pagina.ingresar_email(EMAIL)
    login_pagina.ingresar_password(PASWORD)
    login_pagina.clic_singin()
 
    assert login_pagina.esperar_redireccion_account(), (
        f"Se esperaba redireccion a /account pero la URL es: {login_pagina.url_actual()}"
    )
 
    assert login_pagina.logo_visible(), (
        "El logo de Sauce Demo no esta visible en la pagina /account"
    )
 
    login_pagina.clic_logo()
 
    assert login_pagina.esperar_redireccion_home(), (
        f"Se esperaba redireccion a la home con productos pero la URL es: {login_pagina.url_actual()}"
    )
    print("Login exitoso: usuario accedio a la pagina de productos")
 
 
# ──────────────────────────────────────────
# TC-02: Login Incorrecto (Usuario invalido)
# ──────────────────────────────────────────
def test_login_usuario_invalido(driver):
    """
    Pasos:
        1. Ingresar al portal de inicio
        2. Ingresar un usuario invalido o no registrado
        3. Ingresar una contrasena correcta
        4. Clic en Iniciar Sesion (SIGN IN)
    Resultado esperado:
        El sistema detecta las credenciales invalidas y lanza un mensaje de error
    """
    login_pagina = login(driver)
    login_pagina.abrir_pagina()
    login_pagina.ingresar_email(CREDENCILES_INVALIDAS)
    login_pagina.ingresar_password(PASWORD)
    login_pagina.clic_singin()
 
    assert login_pagina.mensaje_error_visible(), (
        "Se esperaba un mensaje de error con usuario invalido pero no se mostro ninguno"
    )
    print("Login incorrecto (usuario): mensaje de error visible")
 
 
# ──────────────────────────────────────────
# TC-03: Login Incorrecto (Contrasena invalida)
# ──────────────────────────────────────────
def test_login_password_invalida(driver):
    """
    Pasos:
        1. Ingresar al portal de inicio
        2. Ingresar un usuario valido registrado en el sistema
        3. Ingresar una contrasena incorrecta
        4. Clic en Iniciar Sesion (SIGN IN)
    Resultado esperado:
        El sistema detecta las credenciales invalidas y lanza un mensaje de error
    """
    login_pagina = login(driver)
    login_pagina.abrir_pagina()
    login_pagina.ingresar_email(EMAIL)
    login_pagina.ingresar_password(CREDENCILES_INVALIDAS)
    login_pagina.clic_singin()
 
    assert login_pagina.mensaje_error_visible(), (
        "Se esperaba un mensaje de error con contraseña invalida pero no se mostro ninguno"
    )
    print("Login incorrecto por contraseña: tampoco se tiene un mensaje de error visible")
 
 
# ──────────────────────────────────────────
# TC-04: Login Vacio
# ──────────────────────────────────────────
def test_login_vacio(driver):
    """
    Pasos:
        1. Ingresar al portal de inicio
        2. No ingresar usuario ni contrasena
        3. Clic en Iniciar Sesion (SIGN IN)
    Resultado esperado:
        El sistema detecta las credenciales invalidas y lanza un mensaje de error
    """
    login_pagina = login(driver)
    login_pagina.abrir_pagina()
    login_pagina.clic_singin()
 
    assert login_pagina.mensaje_error_visible(), (
        "No hay mensaje de error cuando los campos estan vacios "
    )
    print("Login vacio:no se identifica mensaje de error")
 
 
# ──────────────────────────────────────────
# Test original tuyo — sin modificar
# ──────────────────────────────────────────
def test_login_prueba(driver):
    login_pagina = login(driver)
    assert login_pagina.URL == "https://sauce-demo.myshopify.com/account/login"
    print("URL es correcta")
 