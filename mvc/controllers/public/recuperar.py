import web 
import mvc.controllers.public.firebase_config as token
import pyrebase
import app 
import json

app = web.application(urls, globals())
render = web.template.render("mvc/views/public/")

class Recuperar: 
    def GET(self): 
        message = None
        return render.recuperar(message)

    def POST(self):
        try: 
            message= "0"
            firebase = pyrebase.initialize_app(token.firebaseConfig) 
            auth = firebase.auth() 
            formulario = web.input() 
            email = formulario.email
            auth.send_password_reset_email(email) 
            return web.seeother("/login") 
        except Exception as error:
            formato = json.loads(error.args[1]) 
            error = formato['error'] 
            message = error['message']
            print("Error recuperar.POST: {}".format(message))
            return render.recuperar(message)   