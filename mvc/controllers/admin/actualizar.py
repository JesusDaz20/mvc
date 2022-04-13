import web 
import mvc.firebase_config as token
import pyrebase
import json
import app

render = web.template.render("mvc/views/admin/")


class Actualizar: 
    def GET(self):
         return render.actualizar()

    def POST(self):
        try:
            firebase = pyrebase.initialize_app(token.firebaseConfig)
            auth = firebase.auth() 
            db = firebase.database()
            formulario = web.input()
            name = formulario.name
            phone = formulario.phone
            email = formulario.email
            password= formulario.password
            level = formulario.level
            status = formulario.status
            user = auth.create_user_with_email_and_password(email, password) 
            users = {'name': name,'phone': phone,'email':email, 'level':level, 'status':status} 
            db.child("usuarios").child(user['localId']).set(users) 
            return web.seeother('/usuarios') 
        except Exception as error:
            print("Error actualizar.POST: {}".format(message)) 
            return web.seeother('/usuarios')  
