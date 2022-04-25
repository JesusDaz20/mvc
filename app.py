import web  
import json
import pyrebase
urls = (
    '/', 'mvc.controllers.public.index.Index',
    '/login', 'mvc.controllers.public.login.Login',
    '/logout', 'mvc.controllers.public.logout.Logout',
    '/recuperar', 'mvc.controllers.public.recuperar.Recuperar',
    '/bienvenida_admin', 'mvc.controllers.admin.bienvenida_admin.Bienvenida_admin',
    '/bienvenida_operador', 'mvc.controllers.operadores.bienvenida_operador.Bienvenida_operador',
    '/usuarios', 'mvc.controllers.admin.usuarios.Usuarios',
    '/agregar', 'mvc.controllers.admin.agregar.Agregar',
    '/actualizar', 'mvc.controllers.admin.actualizar.Actualizar',
    '/estado', 'mvc.controllers.admin.estado.Estado',
    '/sucursales', 'mvc.controllers.admin.sucursales.Sucursales',
)

    
app = web.application(urls, globals()) 

if __name__ == "__main__":
    web.config.debug = False 
    app.run()