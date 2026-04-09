import pytest
from pages.login import login
from pages.productos_carrito import productos

 
EMAIL = "cozemik9204@kancwut.my.id"
PASWORD = "laaurora9"
 
NOMBRE = "Jenifer"
APELLIDO = "Varela"
DIRECCION = "Calle 123 # 45-67"
CIUDAD = "Medellin"
PROVIDENCIA = "Antioquia"
CODIGO_POSTAL = "050011"
TARJETA_COMPRA = "4111 1111 1111 1111"
FECHA_TARJETA = "12/25"
CODIGO_TARJETA = "123"
NOMBRE_TARJETA = "Jenifer Varela"
 
 
def login_y_ir_a_productos(driver):
    """Funcion auxiliar: hace login exitoso y navega a la pagina de productos."""
    login_pagina = login(driver)
    login_pagina.abrir_pagina()
    login_pagina.ingresar_email(EMAIL)
    login_pagina.ingresar_password(PASWORD)
    login_pagina.clic_singin()
    login_pagina.esperar_redireccion_account()
    login_pagina.clic_logo()
    login_pagina.esperar_redireccion_home()
 
 
# ──────────────────────────────────────────
# TC-05: Agregar dos productos al carrito
# ──────────────────────────────────────────
def test_agregar_dos_productos_al_carrito(driver):
    """
    Pasos:
        1. Login exitoso y navegar a la pagina de productos
        2. Hacer clic en el primer producto (grey-jacket)
        3. Hacer clic en "Add to Cart"
        4. Volver a la pagina de productos
        5. Seleccionar un segundo producto
        6. Hacer clic en "Add to Cart"
    Resultado esperado:
        El contador del carrito muestra (2)
    """
    login_y_ir_a_productos(driver)
 
    productos_pagina = productos(driver)
 
    # Primer producto
    productos_pagina.clic_primer_producto()
    productos_pagina.clic_add_to_cart()
    print("Primer producto agregado al carrito")
 
    # Volver y agregar segundo producto
    productos_pagina.volver_a_productos()
    productos_pagina.clic_segundo_producto()
    productos_pagina.clic_add_to_cart()
    print("Segundo producto agregado al carrito")
 
# ──────────────────────────────────────────
# TC-06: Finalizar Compra
# ──────────────────────────────────────────
def test_finalizar_compra(driver):
    """
    Pasos:
        1. Login exitoso y navegar a la pagina de productos
        2. Agregar primer producto al carrito
        3. Volver a productos y agregar segundo producto al carrito
        4. Hacer clic en el icono del carrito (My Cart)
        5. Hacer clic en "Check Out"
        6. Llenar el formulario con la informacion solicitada
        7. Hacer clic en "Pay now"
    Resultado esperado:
        La compra se finaliza exitosamente
    """
    login_y_ir_a_productos(driver)
 
    productos_pagina = productos(driver)
 
    # Primer producto
    productos_pagina.clic_primer_producto()
    productos_pagina.clic_add_to_cart()
    print("Primer producto agregado al carrito")
 
    # Segundo producto
    productos_pagina.volver_a_productos()
    productos_pagina.clic_segundo_producto()
    productos_pagina.clic_add_to_cart()
    print("Segundo producto agregado al carrito")
 
    # Abrir carrito y hacer checkout
    productos_pagina.volver_a_productos()
    productos_pagina.clic_icono_carrito()
    productos_pagina.clic_checkout()
 
    assert productos_pagina.esperar_redireccion_checkout(), (
        f"Se esperaba redireccion a /checkouts pero la URL es: {productos_pagina.url_actual()}"
    )
    print(f"Redireccionado a checkout: {productos_pagina.url_actual()}")
 
    # Llenar formulario
    formulario_pagina = (driver)
    formulario_pagina.llenar_nombre(NOMBRE)
    formulario_pagina.llenar_apellido(APELLIDO)
    formulario_pagina.llenar_direccion(DIRECCION)
    formulario_pagina.llenar_ciudad(CIUDAD)
    formulario_pagina.llenar_provincia(PROVIDENCIA)
    formulario_pagina.llenar_codigo_postal(CODIGO_POSTAL)
    formulario_pagina.llenar_tarjeta_compra(TARJETA_COMPRA)
    formulario_pagina.llenar_fecha_expiracion(FECHA_TARJETA)
    formulario_pagina.llenar_codigo_seguridad(CODIGO_TARJETA)
    formulario_pagina.llenar_nombre_tarjeta(NOMBRE_TARJETA)
    print("Formulario de checkout completado")
 
    formulario_pagina.clic_pay_now()
 
    assert formulario_pagina.compra_exitosa(), (
        f"Se esperaba confirmacion de compra exitosa pero la URL es: {formulario_pagina.url_actual()}"
    )
    print("Compra finalizada exitosamente")