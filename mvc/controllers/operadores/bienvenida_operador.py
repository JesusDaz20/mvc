import web 
import mvc.firebase_config as token
import pyrebase
import app 

render = web.template.render("mvc/views/operador/")

class Bienvenida_operador:
    def GET(self): 
        ("Bienvenida.GET localID: ",web.cookies().get('localId'))
        try: 
            ("Bienvenida.GET localID: ",web.cookies().get('localId')) 
            if web.cookies().get('localId') == None: 
                return web.seeother("bienvenida_operador") 
            else: 
                return render.bienvenida_operador() 
        except Exception as error: 
            print("Error Bienvenida.GET: {}".format(error))  