from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class formulario:
    CAMPO_NOMBRE = (By.XPATH, "//input[@id='TextField0']")
    CAMPO_APELLIDO = (By.XPATH, "lastName")
    CAMPO_DIRECCION = (By.XPATH, "//input[@id='TextField3']")
    CAMPO_CIUDAD = (By.XPATH, "//input[@id='TextField5']")
    CAMPO_PROVIDENCIA = (By.XPATH, "//select[@id='Select1']")
    CAMPO_CODIGO_POST = (By.XPATH, "")
    TARJETA_COMPRA = (By.XPATH, "//input[@id='number']")
    FECHA_TARJETA = (By.XPATH, "//input[@id='expiry']")
    CODIGO_TARJETA = (By.XPATH,"//input[@id='verification_value']")
    NOMBRE_TAARJETA = (By.XPATH, "//input[@id='name']")
    BOTON_PAY_NOW = (By.XPATH, "//input[@id='name']") 

    
 
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
 
    def llenar_nombre(self, nombre):
        campo = self.wait.until(EC.visibility_of_element_located(self.CAMPO_NOMBRE))
        campo.send_keys(nombre)
 
    def llenar_apellido(self, apellido):
        campo = self.wait.until(EC.visibility_of_element_located(self.CAMPO_APELLIDO))
        campo.send_keys(apellido)
 
    def llenar_direccion(self, direccion):
        campo = self.wait.until(EC.visibility_of_element_located(self.CAMPO_DIRECCION))
        campo.send_keys(direccion)
 
    def llenar_ciudad(self, ciudad):
        campo = self.wait.until(EC.visibility_of_element_located(self.CAMPO_CIUDAD))
        campo.send_keys(ciudad)
 
    def llenar_providencia(self, providencia):
        campo = self.wait.until(EC.visibility_of_element_located(self.CAMPO_PROVIDENCIA))
        campo.send_keys(providencia)
 
    def llenar_codigo_postal(self,codigo_postal):
        campo = self.wait.until(EC.visibility_of_element_located(self.CAMPO_CODIGO_POST))
        campo.send_keys(codigo_postal)
 
    def llenar_tarjeta_compra(self, tarjeta):
        campo = self.wait.until(EC.visibility_of_element_located(self.TARJETA_COMPRA))
        campo.send_keys(tarjeta)

    def llenar_fecha_tarjeta(self, fecha_tarjeta):
        campo = self.wait.until(EC.visibility_of_element_located(self.FECHA_TARJETA))
        campo.send_keys(fecha_tarjeta)

    def llenar_codigo_tarjeta(self, codigo_tarjeta):
        campo = self.wait.until(EC.visibility_of_element_located(self.CODIGO_TARJETA))
        campo.send_keys(codigo_tarjeta)

    def llenar_nombre_tarjeta(self, nombre_tarjeta):
        campo = self.wait.until(EC.visibility_of_element_located(self.NOMBRE_TAARJETA))
        campo.send_keys(nombre_tarjeta)

    def boton_pay_now(self):
        boton = self.wait.until(EC.element_to_be_clickable(self.BOTON_PAY_NOW))
        boton.click()
 
    
 