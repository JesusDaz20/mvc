import web 
import mvc.firebase_config as token
import pyrebase
import json
import app

render = web.template.render("mvc/views/admin/")


class Agregar: 
    def GET(self):
        message = None
        return render.agregar(message)

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
            return web.seeother('/bienvenida_admin') 
        except Exception as error:
            formato = json.loads(error.args[1])
            error = formato['error']
            message = error['message']
            print("Error agregar.POST: {}".format(message)) 
            return render.agregar(message) 
