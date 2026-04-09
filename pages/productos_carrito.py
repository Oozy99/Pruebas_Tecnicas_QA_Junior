from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
 
class productos:
    URL_PRODUCTOS = "https://sauce-demo.myshopify.com/"
    URL_PRODUCTO_1 = "https://sauce-demo.myshopify.com/collections/frontpage/products/grey-jacket"
    URL_CARRITO = "https://sauce-demo.myshopify.com/cart"
 
    PRIMER_PRODUCTO = (By.XPATH, "//img[@alt='Grey jacket']")
    BOTON_ADD_TO_CART = (By.ID, "add")
    BOTON_VOLVER_PRODUCTOS = (By.XPATH, "//img[@alt='Sauce Demo']")

    
    ICONO_CARRITO_MOBILE = (By.XPATH, "//a[@href='/cart' and contains(@class,'mobile')]")
    ICONO_CARRITO_DESKTOP = (By.XPATH, "//a[@href='/cart' and contains(@class,'desktop')]")
 
    SEGUNDO_PRODUCTO = (By.XPATH, "//img[@alt='Noir jacket']")
 
    ICONO_CARRITO = (By.XPATH, "//a[@href='/cart' and contains(@class,'cart') and contains(@class,'desktop')]")
    CONTADOR_CARRITO = (By.XPATH, "//span[@id='cart-target-mobile']")
    BOTON_CHECKOUT = (By.XPATH, "//input[@value='Check Out']")
 
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
 
    def ir_a_productos(self):
        self.driver.get(self.URL_PRODUCTOS)
 
    def clic_primer_producto(self):
        producto = self.wait.until(EC.element_to_be_clickable(self.PRIMER_PRODUCTO))
        producto.click()
 
    def clic_add_to_cart(self):
        boton = self.wait.until(EC.element_to_be_clickable(self.BOTON_ADD_TO_CART))
        boton.click()
 
    def volver_a_productos(self):
        self.driver.get(self.URL_PRODUCTOS)
 
    def clic_segundo_producto(self):
        producto = self.wait.until(EC.element_to_be_clickable(self.SEGUNDO_PRODUCTO))
        producto.click()
 
    def clic_icono_carrito(self):
        self.driver.get(self.URL_CARRITO)

 
    def clic_checkout(self):
        boton = self.wait.until(EC.element_to_be_clickable(self.BOTON_CHECKOUT))
        boton.click()
 
    def url_actual(self):
        return self.driver.current_url
 
    def esperar_redireccion_checkout(self):
        try:
            self.wait.until(EC.url_contains("/checkouts"))
            return True
        except Exception:
            return False