import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
 
 
# ── Crea la carpeta reports si no existe ──────────────────────────────────────
os.makedirs("reports", exist_ok=True)
 
 
# ── Metadatos que aparecen en la cabecera del reporte HTML ────────────────────
def pytest_configure(config):
    config._metadata = {
        "Proyecto":   "Pruebas Tecnicas QA",
        "Tester":     "Jenifer Varela",
        "Entorno":    "https://sauce-demo.myshopify.com",
        "API Base":   "https://reqres.in/api",
        "Framework":  "Selenium + Pytest",
    }
 
 
# ── Fixture del navegador ─────────────────────────────────────────────────────
@pytest.fixture()
def driver():
    opciones = Options()
    opciones.add_argument("--no-sandbox")
    opciones.add_argument("--disable-dev-shm-usage")
    opciones.add_argument("--window-size=1920,1080")
 
    navegador = webdriver.Chrome(options=opciones)
    navegador.implicitly_wait(5)
    navegador.maximize_window()
 
    yield navegador
 
    navegador.quit()
 
 
# ── Captura screenshot al fallar y lo adjunta al reporte ──────────────────────
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    reporte = outcome.get_result()
 
    # Solo actua en la fase de ejecucion (call) y solo si fallo
    if reporte.when == "call" and reporte.failed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs("reports/screenshots", exist_ok=True)
            nombre = f"reports/screenshots/{item.name}.png"
            driver.save_screenshot(nombre)
 
            # Adjunta el screenshot al reporte HTML
            if hasattr(reporte, "extra"):
                from pytest_html import extras
                reporte.extra = reporte.extra or []
                reporte.extra.append(extras.image(nombre))