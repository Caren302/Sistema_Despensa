import web

class History:
    def GET(self):
        render = web.template.render("mvc/views/historial")
        b=""
        return render.history(b)