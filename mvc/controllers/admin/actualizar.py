import web 
import mvc.firebase_config as token
import pyrebase
import json
import app

render = web.template.render("mvc/views/admin/")


class Actualizar: 
    def GET(self):
        localId = web.cookies().get('localId')
        all_users = db.child("usuarios").get() 
        user = db.child("usuarios").child(localId).get()
        return render.actualizar(user)

    def POST(self):
        firebase = pyrebase.initialize_app(token.firebaseConfig)
        auth = firebase.auth() 
        
        formulario = web.input()
        name = formulario.name
        phone = formulario.phone
        email = formulario.email
        password= formulario.password
        level = formulario.level
        status = formulario.status
        datos_usuarios = {'name': name,'phone': phone,'email':email, 'level':level, 'status':status} 
        db.child("usuarios").child(name).update(datos_usuarios)
        return web.seeother('/usuarios') 
       