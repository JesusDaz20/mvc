import app
import web
 
render = web.template.render('mvc/views/public/') 

class Logout:
    def GET(self):
        return render.logout() 

