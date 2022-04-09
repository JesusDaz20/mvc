import web 
import firebase_config as token
import pyrebase
import json
urls =(
    '/', 'index', 
    '/login', 'Login', 
    '/bienvenida', 'Bienvenida', 
    '/bienvenida_o', 'Bienvenida_o', 
    '/logout', 'logout', 
    '/recuperar', 'Recuperar', 
    '/usuarios', 'Usuarios', 
    '/actualizar', 'Actualizar', 
    '/agregar', 'Agregar', 
    '/sucursales', 'Sucursales', 
    '/sucursales_o', 'Sucursales_o', 
)

index = web.application(urls, globals()) # configura las urls en la aplicacion web
render = web.template.render('mvc/views/admin-operador/') 

class Index:
    def GET(self):
        return render.index()

if __name__ == "__main__":
    web.config.debug = False # Activa  el modo de repuracion de firebase
    index.run() # ejecuta al web app  

