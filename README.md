### Pruebas Tecnicas QA - Sauce Demo & ReqRes API 
## Herramientas Utilizadas 
- Python 3.12
- Selenium -> ayuda a automatizar interfaces web
- Pytest -> Framework para organizar y correr los tests
- Requests -> Generar peticiones a la API 
- pytest-html -> Generar el reporte de resultados en HTML
- ChromeDriver -> Controlador del navegador Chrome

  ## ¿Por qué elegiste ese framework y lenguaje? ##
  Elegi python por que honestamente es el lenguaje con el que me siento mas comoda aprendiendo, y me parecio el leguaje mas apto para empezar en QA.
  
  Tambien elegi ## Selenium ## por que es una de las herramientas mas conocidas en la automatizacion y fue una con las que me empece a involucra inicialmente viendo tutoriales y cursos de QA, También porque es compatible con Python y con Chrome que es el navegador que uso.

  ## Instrucciones para ejecutar las pruebas
  
  ### 1. Clonar o descargar el proyecto
  Clonar o descargar el zip y descomprimirlo

  ### 2. Crear el entorno virtual
  Crea el entorno virtual segun la consola que ustes 
  (Ejem: uso bash -> python -m venv TestEnv
   Activar el entorno -> source TestEnv/Scripts/activate )

  ### 4. Instalar las dependencias
  bash -> pip install -r requirements.txt

  ### 5. Corre las pruebas
  pytest

  ### 6. Ver el reporte 
Cuando termine de correr, abre el archivo `reports/reporte.html` en las carpetas del proyecto
En Windows puedes hacer doble clic sobre ese archivo desde el explorador
  
## Propuesta de mejora
  ### Manejo de datos de prueba
Actualmente los datos como el email, contraseña y datos del formulario están escritos directamente en el código. Lo correcto sería moverlos a un archivo separado `.env` o a un archivo `datos_prueba.json` para no tener credenciales en el código y poder cambiarlos fácilmente sin tocar los tests.

### Linters
Instalaria **flake8** o **pylint** para revisar que el codigo este bien escrito y sin errores de estilo. Por ejemplo, me ayudaría a detectar variables sin usar o líneas muy largas



  
  
  
