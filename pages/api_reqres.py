import requests
class api_reqres:
    URL_BASE = "https://reqres.in/api"
    # Reemplaza este valor con tu API Key real de https://app.reqres.in/
    API_KEY = "reqres_88018024016b494886a9348abf38102e"
 
    HEADERS = {
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }
 
    def get_usuario(self, id_usuario):
        """Consulta un usuario por su ID."""
        url = f"{self.URL_BASE}/users/{id_usuario}"
        respuesta = requests.get(url, headers=self.HEADERS)
        return respuesta
 
    def crear_usuario(self, nombre, trabajo):
        """Crea un nuevo usuario con nombre y trabajo."""
        url = f"{self.URL_BASE}/users"
        cuerpo = {
            "name": nombre,
            "job": trabajo
        }
        respuesta = requests.post(url, json=cuerpo, headers=self.HEADERS)
        return respuesta