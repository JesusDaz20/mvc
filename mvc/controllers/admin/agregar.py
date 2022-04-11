import web 
import mvc.firebase_config as token
import pyrebase
import app 

app = web.application(urls, globals())
render = web.template.render("mvc/views/admin/")


class Agregar: 
    def GET(self):
        return render.agregar(message)

    def POST(self):
        try:
            firebase = pyrebase.initialize_app(token.firebaseConfig)
            auth = firebase.auth() 
            db = firebase.database()
            formulario = web.input()
            nombre = formulario.nombre
            telefono = formulario.telefono
            email = formulario.email
            password= formulario.password
            level = formulario.nivel
            status = formulario.estado
            user = auth.create_user_with_email_and_password(email, password) 
            datos_user = {'nombre': nombre,
                          'telefono': telefono,
                          'email':email, 
                          'nivel':nivel, 
                          'estado':estado} 
            db.child("usuarios").child(user['localId']).set(datos_user) 
            return web.seeother('/bienvenida_admin') 
        except Exception as error:
            formato = json.loads(error.args[1])
            error = formato['error']
            message = error['message']
            print("Error agregar.POST: {}".format(message)) 
            return render.Agregar(message) 