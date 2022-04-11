import app
import web
 
render = web.template.render('mvc/views/public/') 

class Index:
    def GET(self):
        return render.index() 

