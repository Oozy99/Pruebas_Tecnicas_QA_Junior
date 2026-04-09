import requests
import pytest
from pages.api_reqres import api_reqres

 
# ──────────────────────────────────────────
# TC-07: GET - Consultar usuario especifico
# ──────────────────────────────────────────
def test_get_usuario():
    """
    Pasos:
        1. Enviar una peticion GET a /api/users/{id}
        2. Validar que el codigo de respuesta sea 200
        3. Validar que la estructura del JSON tenga los campos esperados
    Resultado esperado:
        Codigo 200 y JSON con campos: data, id, email, first_name, last_name, avatar
    """
    api = api_reqres()
    ID_USUARIO = 2  # usuario que existe en ReqRes
 
    respuesta = api.get_usuario(ID_USUARIO)
 
    # Validar codigo de respuesta
    assert respuesta.status_code == 200, (
        f"Se esperaba codigo 200 pero se recibio: {respuesta.status_code}"
    )
    print(f"Codigo de respuesta: {respuesta.status_code} ✓")
 
    # Convertir la respuesta a JSON
    cuerpo = respuesta.json()
 
    # Validar que exista el campo principal "data"
    assert "data" in cuerpo, (
        f"Se esperaba el campo 'data' en la respuesta pero no estaba. Respuesta: {cuerpo}"
    )
    print(f"Campo 'data' presente ✓")
 
    # Validar los campos dentro de "data"
    data = cuerpo["data"]
 
    assert "id" in data, f"Falta el campo 'id' en data. Data recibida: {data}"
    assert "email" in data, f"Falta el campo 'email' en data. Data recibida: {data}"
    assert "first_name" in data, f"Falta el campo 'first_name' en data. Data recibida: {data}"
    assert "last_name" in data, f"Falta el campo 'last_name' en data. Data recibida: {data}"
    assert "avatar" in data, f"Falta el campo 'avatar' en data. Data recibida: {data}"
    print(f"Estructura del JSON correcta ✓")
 
    # Validar que el id retornado coincida con el solicitado
    assert data["id"] == ID_USUARIO, (
        f"Se esperaba id={ID_USUARIO} pero se recibio id={data['id']}"
    )
    print(f"ID del usuario correcto: {data['id']} ✓")
    print(f"Usuario encontrado: {data['first_name']} {data['last_name']} - {data['email']}")
 
 
# ──────────────────────────────────────────
# TC-08: POST - Crear nuevo usuario
# ──────────────────────────────────────────
def test_crear_usuario():
    """
    Pasos:
        1. Enviar una peticion POST a /api/users con nombre y trabajo
        2. Validar que el codigo de respuesta sea 201
        3. Validar que la respuesta contenga los datos enviados
    Resultado esperado:
        Codigo 201 y JSON con los mismos datos enviados mas id y createdAt
    """
    api = api_reqres()
    NOMBRE = "Jenifer"
    TRABAJO = "QA Engineer"
 
    respuesta = api.crear_usuario(NOMBRE, TRABAJO)
 
    # Validar codigo de respuesta
    assert respuesta.status_code == 201, (
        f"Se esperaba codigo 201 pero se recibio: {respuesta.status_code}"
    )
    print(f"Codigo de respuesta: {respuesta.status_code} ✓")
 
    # Convertir la respuesta a JSON
    cuerpo = respuesta.json()
 
    # Validar que los datos enviados esten en la respuesta
    assert "name" in cuerpo, f"Falta el campo 'name' en la respuesta. Respuesta: {cuerpo}"
    assert "job" in cuerpo, f"Falta el campo 'job' en la respuesta. Respuesta: {cuerpo}"
    assert "id" in cuerpo, f"Falta el campo 'id' en la respuesta. Respuesta: {cuerpo}"
    assert "createdAt" in cuerpo, f"Falta el campo 'createdAt' en la respuesta. Respuesta: {cuerpo}"
    print(f"Estructura del JSON correcta ✓")
 
    # Validar que los datos enviados coincidan con los retornados
    assert cuerpo["name"] == NOMBRE, (
        f"Se esperaba name='{NOMBRE}' pero se recibio name='{cuerpo['name']}'"
    )
    assert cuerpo["job"] == TRABAJO, (
        f"Se esperaba job='{TRABAJO}' pero se recibio job='{cuerpo['job']}'"
    )
    print(f"Datos del usuario creado correctos ✓")
    print(f"Usuario creado: id={cuerpo['id']}, name={cuerpo['name']}, job={cuerpo['job']}, createdAt={cuerpo['createdAt']}")