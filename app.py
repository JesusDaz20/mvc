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
    '/agregar_sucursal', 'mvc.controllers.admin.agregar_sucursal.Agregar_sucursal',
    '/actualizar_sucursal', 'mvc.controllers.admin.actualizar_sucursal.Actualizar_sucursal',
    '/borrar_sucursal', 'mvc.controllers.admin.borrar_sucursal.Borrar_sucursal',
)

    
app = web.application(urls, globals()) 

if __name__ == "__main__":
    web.config.debug = False 
    app.run()